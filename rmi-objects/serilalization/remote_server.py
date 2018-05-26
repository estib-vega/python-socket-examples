class RemoteServer:

    def __init__(self, port):
        self.object_dictionary = {}
        self.port = port

    def bind_object(self, obj, name):
        self.object_dictionary[name] = obj
        print("bound", name, 'to', obj)

    def run(self):
        import socket
        import pickle
        import sys

        PORT = self.port
        with socket.socket() as s:
            s.bind(('localhost', PORT))
            s.listen(1)

            while True:
                print('remote server listening at localhost', PORT, '...')

                try:
                    conn, addr = s.accept()
                    print('accepted connection with:', addr)
                except:
                    print("\nended programm")
                    s.close()
                    sys.exit(1)

                with conn:

                    try:
                        data = conn.recv(1024)
                    except:
                        print("\nended programm")
                        s.close()
                        sys.exit(1)
                    
                    req = data.decode()
                    
                    print('request:', req)

                    # resp = ""

                    # look for the name in the object dictionary
                    if req in self.object_dictionary:
                        resp = pickle.dumps(self.object_dictionary[req])
                    else:
                        resp = b'---object not found'

                    conn.sendall(resp) 







    
