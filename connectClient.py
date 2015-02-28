import socket
import sys

try:
	 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
	print 'Failed to create socket. Error code: '+ str(msg[0]) + ', Erros message: ' + msg[1]
	sys.exit();
print 'Socket Created'
port = 80
host = 'www.google.com'

try:
	remote_ip = socket.gethostbyname(host)
except socket.gaierror:
	print 'Hostname could not be resolved. Exiting'
	sys.exit()
print 'Ip address of ' + host +' is ' +remote_ip

#connect to remote server
s.connect((remote_ip, port))
print 'Socket connected to ' + host + ' on ip' + remote_ip

#send data to remote server
message = "GET / HTTP/1.1\r\n\r\n"

try :
	s.sendall(message)
except socket.error:
	print 'Fail to send'
	sys.exit()
print 'Sending message successfully' 

#receive data
reply = s.recv(4096)
print reply

s.close()

