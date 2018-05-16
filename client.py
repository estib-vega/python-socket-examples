# client
import socket

HOST = 'localhost'
PORT = 1234

with socket.socket() as s: # close after finished
    # stablish connection
    s.connect((HOST, PORT))
    msg = b'Hello World--'
    print("sending message:", msg)
    # attempt to send all data
    s.sendall(msg)
    # receive response in buffered 1024 bytes
    data = s.recv(1024)
    print('received:', data)