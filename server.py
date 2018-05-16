# python socket test
# server
import socket

HOST = 'localhost'
PORT = 1234

with socket.socket() as socket: # close socket after code-block is finished
    # socket object bound to the socket address
    socket.bind((HOST, PORT)) 
    # number of unaccepted connections
    # before start to refusing connections
    # -> one connection at a time
    socket.listen(1)
    print("listening in localhost at port 1234...")
    conn, addr = socket.accept()
    with conn: # close connection after the code-block is finished
        print("initiated connection from:", addr)
        while True:
            # returns the sent data buffered in 1024 bytes
            data = conn.recv(1024)
            if not data: break
            print(data)
            # attempts to send all the data
            conn.sendall(data + b" response")