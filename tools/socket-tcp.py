#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys

host=sys.argv[1]
port_str=sys.argv[2]

try:
    port = int(port_str)
except ValueError:
    print("The second argument shall be an integer")
    sys.exit()


# Socket INET, TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.settimeout(2)
print("connexion faite !")

s.sendall(b'GET /index.html HTML/1.0\r\n\r\n')

while 1:
    try:
        data = s.recv(128)
    except socket.timeout:
        print("Timeout reached while waiting for data")
        break

    if not data:
        break
    print(data)

s.close()
