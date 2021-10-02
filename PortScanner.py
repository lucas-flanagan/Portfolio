#!/usr/bin/python3

import socket
import sys

usage = "Usage: >>python3 PortScanner.py [IP] [common, all, or #]"

if len(sys.argv) != 3:
	print(usage)
	sys.exit()

host = socket.gethostbyname(str(sys.argv[1]))

try:
	scan_type = int(sys.argv[2])
except:
	scan_type = str(sys.argv[2]).upper()

min_port = 0
open_ports = []
single_port_flag = 0

if scan_type == "ALL":
	max_port = 65536
elif scan_type == "COMMON":
	max_port = 1024
elif type(scan_type) == int:
	single_port_flag = 1
	min_port = scan_type
	max_port = scan_type + 1
else:
	print(usage)
	sys.exit()

try:
	for port in range(min_port, max_port):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		res = sock.connect_ex((host, port))
		if res == 0:
			open_ports.append(port)
			print("{} => OPEN".format(port))
		sock.close()
		if (single_port_flag) and res != 0:
			print("{} => CLOSED".format(port))
except KeyboardInterrupt:
	print("\n Exiting..")
except socket.gaierror:
	pritn("Hostname Could Not be Resolved (Check DNS Configuration)")
except socket.error:
	print("Server Offline")