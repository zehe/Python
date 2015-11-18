from socket import *
import thread
import time
serverSocket = socket(AF_INET,SOCK_STREAM)

serverPort = 9187
serverSocket.bind(("",serverPort))
serverSocket.listen(1)

def connectSocket(port):
	