import os
import pandas as pd

input_dir = '../Data/Raw Data'
output_dir = '../Data/Dataset'  
label = 'stand'

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith('.csv'): 
        file_path = os.path.join(input_dir, filename)
        print(f"Processing {filename}...")

        data = pd.read_csv(file_path)

        data = data.iloc[:, 0].str.split(';', expand=True)

        data.columns = ['timestamp', 'MAC', 'subcarrier', 'amplitude', 'phase', 'RSSI', 'frame_control']

        data['subcarrier'] = pd.to_numeric(data['subcarrier'], errors='coerce')
        data['amplitude'] = pd.to_numeric(data['amplitude'], errors='coerce')
        data['phase'] = pd.to_numeric(data['phase'], errors='coerce')

        pivot_data1 = data.pivot(index='timestamp', columns='subcarrier', values='amplitude')
        pivot_data2 = data.pivot(index='timestamp', columns='subcarrier', values='phase')

        pivot_data1.reset_index(inplace=True)
        pivot_data2.reset_index(inplace=True)
        pivot_data1.columns.name = None
        pivot_data2.columns.name = None

        pivot_data1.columns = ['timestamp'] + [f'amplitude_sub{i}' for i in range(256)]
        pivot_data2.columns = ['timestamp'] + [f'phase_sub{i}' for i in range(256)]

        merged_data = pivot_data1.merge(pivot_data2, on='timestamp', how='inner')

        merged_data['label'] = label

        output_file_path = os.path.join(output_dir, filename)
        merged_data.to_csv(output_file_path, index=False)

        print(f"Transformed data saved to {output_file_path}.")
