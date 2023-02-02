Name: Pujita Bodapati

EMAIL : nbodapa1@binghamton.edu

B-NO  : B00929285

***The code was tested on remote.cs.binghamton.edu and it works***

***To compile and execute the program:***

***Server program:***
python3 server.py 9285

***Client Program:***
python3 client.py remote05 9285

***Note:***
* To get the list of files present in server the client must send 'ls' command and once server receives the message it sends the corresponding files present to client side and client will print it to the user. (For clear scenario - I have created 2 sample files in
server side 'sample1.txt' and 'sample2.txt').
* To get the path send 'pwd' command on client to server
* To terminate the connection 'exit' command is used.
* If any message other that 'pwd' or 'ls' or 'exit' will be used, the connection will be terminated
