## Data Format

- The dataset includes activities labeled as `empty`, `fall`, `run`, `stand`, and `walk`. Each activity was performed for a maximum duration of **5 minutes** and collected from **5 individuals**.  

- Data was collecte under both **Line-of-Sight (LoS)** and **Non-Line-of-Sight (nLoS)** scenarios.  

- The data was originally collected in `.pcap` format and later converted to `.csv` format. We used script made available by [cheeseBG](https://github.com/cheeseBG/pcap-to-csv).

- [Raw Data](./Raw%20Data/): Raw data with no preprocessing.

- [Dataset](./Dataset/): Preprocessed data containing only `amplitude` data with respective labels for training the model.
---
### ⚠ Important:
 - The provided dataset is intended exclusively for **demonstration purposes**, enabling users to run model training and understand the preprocessing pipeline in this project. 

 - It is not intended for performance benchmarking.

 - The dataset contains CSI data before preprocessing.
