# Student README

## Questions

1. The client and server have different sized buffers.  Why does it still work?

2. What happens if the buffer size on the client is changed to a value smaller than the initial `message_length`?

3. What happens if you run the client when the server is not running? 

4. What happens if you run the server while the server is already running?

5. What changes did you make to finish this assignment?

6. What resources did you use to complete this assignemnt?  Make a Markdown list of web links below.

## Answers

1. server / client don't care the buffer size of the client / server .

2. the message_lenght divides.

3. ConnectionRefusedError happens.

4. OSError happens.

5. changes 
   1= running while loop from accepting from the connection 
   2= added if in for the password   
  
6. net-information url: 'http://net-informations.com/python/net/socket.htm'.
   realpython url: 'https://realpython.com/python-sockets/'.   
