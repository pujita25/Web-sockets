# first of all import the socket library
import socket
import sys
import ssl
import os
arglen=len(sys.argv)
if arglen!=2:
	print('input arguments incorrect. The correct format should be python3 "<filename> <port number>" ')
	quit()
#creating a socket object using SSL context
context = ssl.create_default_context()
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('../cert.pem', '../key.pem')
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
print ("The connection is successfully setup....")
# reserve a port from the command line
port = int(sys.argv[1])
# Next bind to the port
s.bind(('', port))
print ("The socket is binded to the following port: %s" %(port))
# put the socket into listening mode
s.listen(1)
print ("Now, the socket is listening")
BUF_SIZE=1000
# a forever loop until we interrupt it or
# an error occurs
c, addr = s.accept()
print('Received the connection from::', addr)
# send a thank you message to the client. encoding to send byte type.
c.send('Sending message from server to client. Successfully setup.....'.encode())
while True:   
    data = (c.recv(BUF_SIZE)).decode()
    if(data=='pwd'):
        c.send(os.getcwd().encode())
    elif(data=='ls'):
        strng = ''
        for path, subdirs, files in os.walk(os.getcwd()):
            for name in files:
                strng += os.path.join(path, name) + '\n'
        c.send(strng.encode())
    elif(data=='exit'):
    	print('Terminating the server. Received msg from client - exit...\n')
    	break
    else:
        break
    
    # Close the connection with the client
c.close()
    # Breaking once connection closed
