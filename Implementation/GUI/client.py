import pcap
import dpkt
import keyboard
import pandas as pd
import numpy as np
import os
from datetime import datetime
import time
import socket
import pickle

# For send CSI data(server IP/Port)
HOST = '192.168.0.101'
PORT = 1111


# for sampling
def truncate(num, n):
    integer = int(num * (10 ** n)) / (10 ** n)
    return float(integer)


def sniffing(nicname):
    print('Start Sniifing... @', nicname, 'UDP, Port 5500')
    sniffer = pcap.pcap(name=nicname, promisc=True, immediate=True, timeout_ms=50)
    sniffer.setfilter('udp and port 5500')

    before_ts = 0.0

    for ts, pkt in sniffer:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            if int(ts) == int(before_ts):
                cur_ts = truncate(ts, 1)
                bef_ts = truncate(before_ts, 1)

                if cur_ts == bef_ts:
                    before_ts = ts
                    continue

            eth = dpkt.ethernet.Ethernet(pkt)
            ip = eth.data
            udp = ip.data

            mac = udp.data[4:10].hex()

         
      
            csi = udp.data[18:]

            bandwidth = ip.__hdr__[2][2]
            nsub = int(bandwidth * 3.2)

      
            csi_np = np.frombuffer(
                csi,
                dtype=np.int16,
                count=nsub * 2
            )


            csi_np = csi_np.reshape((1, nsub * 2))


            csi_cmplx = np.fft.fftshift(
                csi_np[:1, ::2] + 1.j * csi_np[:1, 1::2], axes=(1,)
            )
            
            csi_amp = list(np.abs(csi_cmplx)[0])
            csi_data = pickle.dumps(csi_amp)
            
            try:
                sock.connect((HOST, PORT))
                sock.sendall(csi_data)
            finally:
                sock.close()

            before_ts = ts

            if keyboard.is_pressed('s'):
                print("Stop Collecting...")
                break


if __name__ == '__main__':
    sniffing('wlan0')
