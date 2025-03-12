# CSIServer
A simple CSI Server for Nexmon-based Raspberry Pi Setups
This software will gather the packets from NEXMON and make them available for real-time streaming via a TCP socket.

### Usage:
- Compile using `make` in CSIServer/ folder.
- Run command on your Raspberry Pi:
    ```bash
        ./CSIServer_ng
    ```
    It will dump UDP packets coming from nexmon on port 5000.
- At the same time, it will listen on TCP port 5001. CSIStudio will connect to the CSI Server.


 
