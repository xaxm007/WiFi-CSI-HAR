## Data Format

- The dataset includes activities labeled as `empty`, `stand`, and `walk`. Each activity was performed for a maximum duration of **5 minutes** and collected from **4 individuals**.  

- Data was collecte under **Line-of-Sight (LoS)** scenarios.  

- The data was collected using application [WirelessEye](https://github.com/pkindt/WirelessEye).

- [Raw Data](./Raw%20Data/): Collected data with default preprocessing included from referenced application in specified SimpleCSV format.

- [Dataset](./Dataset/): Preprocessed data containing `timestamp`, `MAC address` `amplitude` & ' `phase` data with respective labels in column-wise subcarrier format for training the model.
---
### ⚠ Important:
 - The provided dataset is intended exclusively for **demonstration purposes**, enabling users to run model training and understand the preprocessing pipeline in this project. 

 - It is not intended for performance benchmarking.

 - `The dataset will be made available upon request via Email.`
