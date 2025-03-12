# CSIStudio

Qt GUI for PC to connect to Raspberry Pi via TCP and record CSI data and run real-time classification.

## Usage:

- Compile [make](./src/filters/Makefile) in src/filters folder to load all the filters.
- Run `qmake` in studio/ folder.
- Compile [make](./Makefile) in studio/ folder to compile the c/c++ files.
- Run command:
    ```bash
        ./WirelessEye
    ```

1. In the tab _settings->connection_, enter the IP address of your Raspberry Pi. In _settings->CSI, adjust the bandwith you selected when running Nexmon.

2. In the tab _visualization_, click _connect_. Upon success, the text in the button will change to "connected" and data is being streamed from the Raspberry Pi.

3. In the _settings->recording_, select _static filename_ to rename different csv files to store and select _Simple CSV_ format similar to this project's data recording format. The [fileFormats](./fileFormats.pdf) document can be accessed from the given link.

5. In the tab, _real-time classification_ to run classifier load the trained model in [realtime.py](./realtime.py) file.