import warnings
import pandas as pd
import os
import sys
import tensorflow as tf
from datetime import datetime
from multiprocessing.pool import ThreadPool

tf.config.set_visible_devices([], 'GPU')

warnings.filterwarnings('ignore')  # Suppress tensorflow logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress errors log


def classify(classifier, window):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    labels = {
        0: 'empty',
        1: 'stand',
        2: 'walk',
    }

    prediction = classifier.predict(window)
    pred_label = prediction.argmax(1)[0]
    pred_porb = prediction[0][pred_label]

    log_message = f'{current_time} --> {labels[pred_label]} (acc: {round(pred_porb, 2)})'
    print(log_message, file=sys.stderr)
    return log_message

if __name__ == '__main__':

    buffer = ''
    separator = ';'
    sampling_frequency = 14 # Hz
    time_window_size = sampling_frequency * 2 # s
    pool = ThreadPool(processes=1)
    df_realtime = pd.DataFrame()

    # Load the trained model
    model = tf.keras.models.load_model('model.keras')

    sys.stdout.buffer.write(bytes([0xca, 0xff, 0xee]))
    sys.stdout.flush()

    while True:

        buffer += sys.stdin.readline()

        if buffer.endswith('\n'):
            line = buffer[:-1]
            buffer = ''


            time, mac, sub, amp, phase, rssi, fc = str(line).split(';')
            time = pd.to_datetime(str(pd.to_datetime(':'.join(time.split(':')[:-1]) + '.' + time.split(':')[-1])))
            amp = float(amp.replace(',', '.'))
            df_realtime.at[time, f'sub ({sub})'] = amp

            if df_realtime.shape[0] == time_window_size and not df_realtime.isnull().values.any():
                df_realtime = df_realtime.values.reshape((1, df_realtime.shape[0], df_realtime.shape[1]))

                async_result = pool.apply_async(classify, (model, df_realtime))

                print('%s' % async_result.get())
                sys.stdout.flush()
                df_realtime = pd.DataFrame()
