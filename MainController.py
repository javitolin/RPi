#!/usr/bin/python
from multiprocessing import Process, Lock
import sys
from TcpServer import *
from time import sleep

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("add argument: tcp")
		exit()
	arg = sys.argv[1]
	tcpProcess = Process(target=StartTCPServer)
	if arg == "tcp":
		tcpProcess.start()
	else:
		print("Invalid argument: "+arg)