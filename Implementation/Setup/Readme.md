# Hardware Setup

- [Nexmon_CSI](https://github.com/seemoo-lab/nexmon_csi) is a project that allows you to extract channel state information (CSI) of OFDM-modulated Wi-Fi frames `(802.11a/(g)/n/ac)` on a per frame basis with up to 80 MHz bandwidth on the `Broadcom` Wi-Fi Chips.

- Installation on **Raspberry Pi 4B (Chip: BCM43455c0) `kernel version: 5.10.92`** followed documentation by [nexmonster](https://github.com/nexmonster/nexmon_csi/tree/pi-5.10.92) for using [Nexmon_CSI](https://github.com/seemoo-lab/nexmon_csi).

- For extracting CSI, we used MAC filter for our [MikroTik-SXT2](<../../Reference Papers/Related Works/MikroTik.pdf>) Router.
    - 20 MHz Bandwidth
    - 2.4 GHz Band
    - IEEE 802.11n protocol i.e. 11b/g/n
    - Channel 6
    - No. of Subcarriers  = 3.2 * Bandwidth(20) = 64

- Use mcp to generate a base64 encoded parameter string `hexcode` which is used to configure extractor to collect CSI on `channel 6` with `bandwidth 20 MHz` from `MAC: 6c:bf:6e:4c:7a:21`.
    ```bash
    mcp -C 1 -N 1 -c 6/20 -m 6c:bf:6e:4c:7a:21

    BhABEQAAAQBsO2uu+SEAAAAAAAAAAAAAAAAAAAAAAAAAAA==
    ```

- Run [Script](./start.sh) with the `hexcode` configured, to enable monitor mode and firmware to extract CSI from specified Router's Wi-Fi signals.

- Collect CSI by listening on socket `5500` for UDP packets and store `2000` CSI samples in a pcap file `output.pcap`. 
    ```
    tcpdump -i wlan0 dst port 5500 -vv -w output.pcap -c 2000
    ```

## ⚠️ Important: 
- You will not be able to use the built in WiFi chip to connect to your WLAN, so use an Ethernet cable.