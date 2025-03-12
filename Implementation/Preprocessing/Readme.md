# Preprocessing

- CSI data is recorded in SimpleCSV format using [WirelessEye](https://github.com/pkindt/WirelessEye).

- Nulling `Null` and `Guard` subcarrier columns via the reference application, resulting in columns of only `Data` and `Pilot` subcarriers containing actual data. 

- Subcarrier Nulling based on `IEEE 802.11ac` protocol for `80 MHz bandwidth`.

- [Conversion](./conversion.py): Transforms data file in column-wise subcarrier data format for model training stored in [Dataset](../Data/Dataset/) folder.

- [Preprocessing](./Preprocessing.ipynb): Visualization for Hampel Filter & DWT based on [v1.0](https://github.com/xaxm007/WiFi-CSI-HAR/tree/SXT2) code after Subcarrier Removal for filter output comparison and data analysis. 

- [Visualization](./Visualization.ipynb): Detailed Visualization for Hampel & DWT.

## Requirements
The requirements to run this code are:
- Altair
- Matplotlib
- Numpy
- Pandas
- Pywavelets