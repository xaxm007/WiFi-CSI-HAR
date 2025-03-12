# CSI-HAR (UI)

Developed using C/C++, Qt library for data collection and activity classification output display.

### Prerequisites

- A Raspberry PI 4B [with kernel version 5.10](https://downloads.raspberrypi.org/raspios_lite_armhf/images/raspios_lite_armhf-2022-01-28/) with Nexmon firmware
- A Linux PC or Laptop (Ubuntu, Arch)
- The GNU C compiler (GCC) for PC and Raspberry Pi
- GNU make for PC and Raspberry Pi
- QT library version 5 for PC
- QTCreator IDE for UI in PC.
- WiFi AP to create some WiFi signals to capture CSI

### Components

- CSIServer_ng:
    A simple TCP server to be run on the Raspberry PI. 
    It will receive the UDP broadcasts from Nexmon and make them available over the network via TCP port 5501

- Studio:
    A Qt GUI to display, record and export CSI data in real-time. To be run on any Linux PC from which the Raspberry Pi that runs the CSIServer is reachable over the network.

## Acknowladgements

Refer to the original repository [WirelessEye](https://github.com/pkindt/WirelessEye) for additional resources.