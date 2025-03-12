# Hardware Setup

- [Nexmon_CSI](https://github.com/seemoo-lab/nexmon_csi) is a project that allows you to extract channel state information (CSI) of OFDM-modulated Wi-Fi frames `(802.11a/(g)/n/ac)` on a per frame basis with up to 80 MHz bandwidth on the `Broadcom` Wi-Fi Chips.

- Installation on **Raspberry Pi 4B (Chip: BCM43455c0) `kernel version: 5.10.92`** followed documentation by [nexmonster](https://github.com/nexmonster/nexmon_csi/tree/pi-5.10.92) for using [Nexmon_CSI](https://github.com/seemoo-lab/nexmon_csi).

- For extracting CSI, we used MAC filter for our [TP-Link Archer C6 AC1200](https://openwrt.org/toh/tp-link/archer_c6_v3) Router.
    - 80 MHz Bandwidth
    - 5 GHz Frequency Band
    - IEEE 802.11ac protocol i.e. 11a/ac
    - Channel 149
    - No. of Subcarriers  = 3.2 * Bandwidth(80) = 256

- Use mcp to generate a base64 encoded parameter string `hexcode` which is used to configure extractor to collect CSI on `channel 149` with `bandwidth 80 MHz` from `MAC: 28:87:ba:a1:9a:d2`.
    ```bash
    mcp -C 1 -N 1 -c 149/80 -m 28:87:ba:a1:9a:d2

    BhABEQAAAQBsO2uu+SEAAAAAAAAAAAAAAAAAAAAAAAAAAA==
    ```

- Run [Script](./start.sh) with the `hexcode` configured, to enable monitor mode and firmware to extract CSI from specified Router's Wi-Fi signals.

<!-- - Collect CSI by listening on socket `5500` for UDP packets and store `3500` CSI samples in a pcap file `output.pcap`. 
    ```
    tcpdump -i wlan0 dst port 5500 -vv -w output.pcap -c 3500
    ``` -->

## ⚠️ Important: 
- You will not be able to use the built in WiFi chip to connect to your WLAN, so use an Ethernet cable.