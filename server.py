import socket

HOST = '127.0.0.1'
PORT = 1027
BUFFER_SIZE = 512

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn,addr = s.accept()
        with conn:
            print('connection opened by', addr)
            full_message = bytearray()
            data = conn.recv(BUFFER_SIZE)
            full_message += data
            if data == b'password':
                conn.sendall(bytes("enter now", 'UTF-8'))
            elif not data: # if no data, break from loop
                break
            conn.sendall(data)
    
        print("Connection closed")
