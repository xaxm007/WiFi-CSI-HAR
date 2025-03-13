# Usage

- [Prepare](./Setup/) Raspberry Pi with Nexmon Firmware. 

- Setup [CSIServer](./UI/CSIServer/) on RPi and [CSIStudio](./UI/CSIStudio/) on Linux PC or Laptop (Client).

- Collect CSI Data of specified Router with MAC from the Client with Laptop sending ping packet to the Router for channel traffic.

- Perform [preprocessing](./Preprocessing/) by first converting the recorded data to trainable dataset format and visualize the preprocessed data for verification of each data.

- [Train](./Model/) a model to classify defined activities.

- [Add model](./UI/CSIStudio/realtime.py) to real-time classifier file for classifer output in the UI.