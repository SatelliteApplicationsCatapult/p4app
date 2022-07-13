import socket
import struct


UDP_IP = "0.0.0.0"
UDP_PORT = 2152

sock = socket.socket(socket.AF_INET,    # Internet
                     socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, UDP_PORT))

while True:
    data, src = sock.recvfrom(1024) # buffer size is 1024 bytes
    ip_addr, port = src
    _, _, _, teid, _, _, _, _ = struct.unpack('>ccHIcccc', data)

    print("Received GTP message with TEID %d from %s" %(teid, ip_addr))
