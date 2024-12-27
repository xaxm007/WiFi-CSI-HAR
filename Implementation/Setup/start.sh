ifconfig wlan0 up

nexutil -Iwlan0 -s500 -b -l34 -vKuABEQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==

iw dev wlan0 interface add mon0 type monitor

ip link set mon0 up