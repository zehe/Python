from socket import *
serverName = input("Type in the serverName")
serverPort = int(input("Type in the serverPort"))
fileName = input("Type in the fileName")

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
clientSocket.send(fileName)
inforGet = clientSocket.recv(1024)
print 'From Server:',inforGet
clientSocket.close()