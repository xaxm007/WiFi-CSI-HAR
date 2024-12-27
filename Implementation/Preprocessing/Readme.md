# Preprocessing

- CSI data is in complex form of Amplitude and Phase (amplitude +i phase).

- Resolve only Amplitude data of all subcarriers into columns for now.

- Drop `Null`, `Pilot` and `Guard` subcarrier columns resulting in columns of only `Data` subcarriers. 

- Subcarrier Removal based on `IEEE 802.11n` protocol.

- Hampel Filter for outlier removal & Discrete Wavelet Transform for denoising.

- [Preprocessing](./Preprocessing.ipynb): Preprocessing using Subcarrier Removal, Outlier removal (Hampel), Denoising (DWT) and  on the data subcarriers.

## Requirements
The requirements to run this code are:
- Altair
- Matplotlib
- Numpy
- Pandas
- Pywavelets