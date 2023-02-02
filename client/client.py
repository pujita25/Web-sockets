# Import socket module
import socket			
import sys
import ssl
BUF_SIZE = 1024
arglen=len(sys.argv)
if arglen!=3:
	print('The input arguments incorrect. The correct format should be "python3 <filename> <Domain name> <port number>" ')
	quit()
# Create a socket object
context = ssl.create_default_context()
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('../cert.pem', '../key.pem')
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
# Define the port on which you want to connect
port = int(sys.argv[2])			
# connect to the server on local computer
s.connect((sys.argv[1], port))
data = (s.recv(BUF_SIZE)).decode()
#print ('\n data received from the server is \n')
print(data)
while True:
	MSG=input('ssh>')
	# receive data from the server and decoding to get the string.
	if (MSG=='pwd'):
		s.send(MSG.encode())
		print((s.recv(BUF_SIZE)).decode())
	elif(MSG=='ls'):
		s.send(MSG.encode())
		files = (s.recv(BUF_SIZE)).decode()
		print(files)
	elif (MSG=='exit'):
		s.send(MSG.encode())
		break
	else:
		print('Invalid command ')
		break
s.close()

