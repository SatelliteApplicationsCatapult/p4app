import sys

from scapy.all import *
from scapy.contrib.gtp import GTP_U_Header
from time import sleep


if __name__ == '__main__':
    if len(sys.argv) == 3:
        while True:
            p = IP(
                version=4,
                dst=sys.argv[1]) / \
                UDP(
                    sport=2152,
                    dport=2152) / \
                GTP_U_Header(
                    version=1, PT=1, reserved=0, E=1, S=0, PN=0,
                    gtp_type="g_pdu",
                    teid=int(sys.argv[2]),
                    seq=0x0,
                    npdu=0,
                    next_ex=133
                )
            send(p)
            sleep(2)
    else:
        print("Usage: gtp_gnb.py <IP dest> <TEID>")
