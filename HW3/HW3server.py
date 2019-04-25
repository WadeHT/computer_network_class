from socket import *
from os import listdir
serverPort = 12000
host = gethostname()
print('host name = ',host)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((host,serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')
while True:
     connectionSocket, addr = serverSocket.accept()     
     sentence = connectionSocket.recv(1024).decode()
     print('From addr = ',addr[0],' port = ',addr[1])
     print('receive = ',sentence)
     sentence.split()
     file = sentence.split(' ',1)[1]
     anserSentence =  'error'
     for i in listdir('.'):
          if i == file:
               context = open(file,'r')
               anserSentence = context.read()
               break
     connectionSocket.send(anserSentence.encode())
     connectionSocket.close()
