#import socket module
from socket import *
serverSocket = socket(AF_INET,SOCK_STREAM)
#perpare a server socket

#Fill in start
serverPort = 9187
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
#Fill in end

while True:
	#Establish the connection
	print 'Ready to serve....'
	#Fill in start
	connectionSocket,addr = serverSocket.accept()
	#Fill in end
	try:
		#Fill in start
		message = connectionSocket.recv(1024)
		#Fill in end
		filename = message.split()[1]
		f = open(filename[1:])
		#Fill in start
		outputdata = f.read()
		#Fill in end

		#Send one HTTP header line into socket
		#Fill in start
		connectionSocket.send("HTTP/1.1 200 We got this html page!!!\r\n\r\n")
		#Fill in end
		# Send the content of the requested file to the connection socket
		for i in range(0, len(outputdata)):  
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
	except IOError:
		# Send HTTP response message for file not found

		#Fill in start
		connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
		connectionSocket.send("<html><head></head><body><h1>Sorry, The page you are looking for isn't exist!!!</h1></body></html>\r\n")
		#Fill in end

		# Close the client socket
		#Fill in start
		connectionSocket.close()
		#Fill in end

serverSocket.close()

