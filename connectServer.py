import socket
import sys
from thread import * #use thread to handle communication for a connection accepted by server, so the main server accept more connections

HOST = '' #All avaliable  interfaces
PORT = 8888 # use non-previleged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
	s.bind((HOST, PORT))
except socket.error, msg:
	print 'Bind failed. Error code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
print 'Socket bind complete'

#listen incoming connections
s.listen(10) # 10 means backlog, 10 conections are waiting to be processed and 11th connection request will be rejected when the program is busy
print 'Socket is now listening' 

#Part 1 
#uncomment below code, connection will be closed immediately after server accepts and sends reply
'''#accept new connections
conn, addr = s.accept()
#show the information of client
print 'Connected with ' + addr[0] + ':' + str(addr[1])

#continue to talk with client after establishing the connection
data = conn.recv(1024)
conn.sendall(data)'''

#Part 2
'''#uncomment this part, server handles only one connection a time
#make server running non-stop
while 1:
	conn, addr = s.accept()
	print 'Connected with ' + addr[0] + ':' + str(addr[1])
	
	data = conn.recv(1024)
	reply = 'OK...' + data
	if not data:
		break
	conn.sendall(reply)'''

#Part 3
#create threads to let server handle multiple connections a time
def thread(conn):
	#send message to connected client
	conn.send('Welcome to server. Type something\n')
	
	#build a loop that function not terminate and thread not end
	while True:
		#receive data from client 
		data = conn.recv(1024)
		reply = 'OK...' + data
		if not data:
			break
		conn.sendall(reply)
	conn.close()
#keep talk with the client 
while 1:
	conn, addr = s.accept()
	print 'Connect with ' + addr[0] + ':' + str(addr[1])
	#start a new thread 
	start_new_thread(thread, (conn,))
s.close()

