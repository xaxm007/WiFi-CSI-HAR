import socket
import time
import csi.pcapTodf as decoder
import pandas as pd
from preprocess.process import main
from model.inference import InferenceServer
from queue import Queue

# Server settings
TCP_IP = "192.168.0.100"
TCP_PORT = 5502
BUFFER_SIZE = 512 * 4
bandwidth = 20
labels = ["noactivity", "stand", "walk"]

# Queue for thread-safe communication between server and GUI
prediction_queue = Queue()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((TCP_IP, TCP_PORT))
        s.listen(1)
        print("Waiting for connections...")
        conn, addr = s.accept()
        print("Connected by", addr)
        conn.settimeout(10)

        frame_count = 0
        frames_list = []

        while True:
            try:
                frame = conn.recv(BUFFER_SIZE)

                if len(frame) < (18 + int(bandwidth * 3.2) * 4):
                    print(f"Frame too small: {len(frame)} bytes. Skipping...")
                    continue

                frame_info = decoder.pcap_to_df(frame, bandwidth)
                if frame_info is None:
                    print("Invalid frame received. Skipping...")
                    continue

                frames_list.append(frame_info)

                if frame_count % 22 == 0 and frame_count > 0:
                    compiled_df = pd.concat(frames_list, ignore_index=True)
                    processed_data = main(compiled_df)
                    predict = InferenceServer()
                    result = predict.inference(processed_data)
                    prediction_queue.put(labels[result])
                    frames_list.clear()

                frame_count += 1
                print(frame_count)

            except socket.timeout:
                print("Socket timeout. No data received.")
            except Exception as e:
                print(f"Error: {e}")
                break