#!/usr/bin/python
from multiprocessing import Process, Lock
import sys
from IRServer import *
from TcpServer import *
from BluetoothServer import *
from time import sleep

def mainProcessFunc():
    while 1:
    	print ("Main still working")
    	sleep(2)


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("add argument: tcp or bt")
		exit()
	arg = sys.argv[1]
	irProcess = Process(target=StartIRServer)
	tcpProcess = Process(target=StartTCPServer)
	btServer = Process(target=startBluetoothServer)
	mainProcess = Process(target=mainProcessFunc)
	#irProcess.start()
	if arg == "tcp":
		tcpProcess.start()
	elif arg == "bt":
		btServer.start()
	else:
		print("Invalid argument: "+arg)