import socket

# listening to nexmon_csi on port 5500
UDP_IP = "255.255.255.255"
UDP_PORT = 5500

# preparing udp server on rpi
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:

    sock.bind((UDP_IP, UDP_PORT))

    # connecting to the PC server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_pc:
        server_pc.connect(('192.168.0.100', 5502))

        while True:
            try:
                print("sending data")
                data, addr = sock.recvfrom(512 * 4)  # buffer size is 2048 + 18 bytes
                server_pc.sendall(data)
                print("sent")
            except ConnectionError as e:
                decision = input("Server down. Reconnect? ([y]/n) ")
                if decision in ["n", "N"]:
                    exit(0)
                else:
                    continue
