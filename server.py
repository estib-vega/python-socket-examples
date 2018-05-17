# python socket test
# server

def connection_handler(conn, addr, c):
    print("initiated connection from:", addr)
    with conn:
        while True:
            # returns the sent data buffered in 1024 bytes
            data = conn.recv(16)

            if not data: break # end current connection

            print(data.decode())

            response = -1

            # interpret command
            command = data.decode()
            if command == "i":
                print("increment")
                response = c.increment()
            elif command == "r":
                print("reset")
                response = c.reset()
            elif command == "d":
                print("decrement")
                response = c.decrement()
            else:
                print("not yet suppported... sry")
            
            conn.sendall(response.to_bytes(16, byteorder=sys.byteorder, signed=True))
            return

if __name__ == '__main__':
    import socket
    import sys
    from counter import Counter
    import _thread as t

    c = Counter()

    if len(sys.argv) != 2:
        print("should have a port as argument...")
        sys.exit(1)

    HOST = 'localhost'
    PORT = int(sys.argv[1])

    with socket.socket() as socket: # close socket after code-block is finished
        # socket object bound to the socket address
        socket.bind((HOST, PORT)) 

        # number of unaccepted connections
        # before start to refusing connections
        # -> one connection at a time
        socket.listen(2)

        # outter loop for running sequentially for every request
        while True:
            
            print("listening in localhost at port", PORT, "...")

            conn, addr = socket.accept()

            t.start_new_thread(connection_handler, (conn, addr, c))