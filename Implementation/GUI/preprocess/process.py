import pandas as pd
import numpy as np
import pywt

SUBCARRIES_NUM = 52

def remove_columns(df):
    columns_to_remove =  [0,1,2,3,32,61,62,63,11,25,39,53, 60] #['0', '1', '2', '3', '32', '61', '62', '63', '11', '25', '39', '53']

    return df.drop(columns=columns_to_remove)

def hampel(vals_orig, k=11, t0=3, outliers_return=False):
    vals = pd.Series(vals_orig.copy())

    # HAMPEL FILTER
    L = 1.4826

    rolling_median = vals.rolling(k).median()
    difference = np.abs(rolling_median - vals)
    median_abs_deviation = difference.rolling(k).median()
    threshold = t0 * L * median_abs_deviation
    outlier_idx = difference > threshold
    vals[outlier_idx] = rolling_median

    if outliers_return:
        return vals, outlier_idx

    return vals

def denoise(vals, th=0.25):
    threshold = th  # THRESHOLD OF FILTERING

    data = vals.copy()

    w = pywt.Wavelet('sym4')
    maxlev = pywt.dwt_max_level(data.shape[0], w.dec_len)
    coeffs = pywt.wavedec(data, 'sym4', level=maxlev)

    for i in range(1, len(coeffs)):
        coeffs[i] = pywt.threshold(coeffs[i], threshold * max(coeffs[i]), mode='soft')

    datarec = pywt.waverec(coeffs, 'sym4')

    return datarec

def filter_amplitude_all_subcarriers(amplitudes):
    data_len = amplitudes.shape[0]

    res = np.zeros_like(amplitudes)

    for i in range(amplitudes.shape[1]):
        res[:data_len, i] = denoise(hampel(amplitudes[:, i]))[:data_len]

    return res

def read_csi_data_from_csv(filtered):
    data = pd.DataFrame(filtered).apply(pd.to_numeric, errors='coerce').values
    data = np.nan_to_num(data)
    return data

def amplitude_only(df):
    amplitudes = pd.DataFrame()
    for col in df.columns[1:]:
        #complex_numbers = df[col].apply(lambda x: complex(x.strip("()")))
        complex_numbers = df[col].apply(lambda x: x if isinstance(x, complex) else complex(x.strip("()")))
        amplitudes[col] = np.abs(complex_numbers)

    filtered_amplitudes = remove_columns(amplitudes)
    amp = read_csi_data_from_csv(filtered_amplitudes)
    result = filter_amplitude_all_subcarriers(amp)
    return result

def main(frame):  # Accept frame as an argument
    complete = pd.DataFrame(amplitude_only(frame))
    return complete

# This will allow this file to be imported without executing the main block
if __name__ == "__main__":
    pass