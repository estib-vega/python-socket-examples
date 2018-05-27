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

                    req_list = list(req.split('-'))

                    if len(req_list) == 1:
                        # look for the name in the object dictionary
                        if req in self.object_dictionary:
                            resp = pickle.dumps(self.object_dictionary[req])
                        else:
                            resp = b'---object not found'
                    elif len(req_list) == 4:
                        # if the request has multiple arguments
                        # then it means it's a method call

                        # used for argument parsing 
                        # str -> tuple
                        # str -> dict
                        from ast import literal_eval

                        # the first parameter must be a dictionary key
                        obj_name, a, k, method = tuple(req_list)

                        if not obj_name in self.object_dictionary:
                            resp = b'---object not found'
                            conn.sendall(resp)
                            continue
                        
                        # the arguments must be a valid tuple and a valid dictionary
                        args = literal_eval(a)
                        kwargs = literal_eval(k)

                        obj = self.object_dictionary[obj_name]

                        if not hasattr(obj, method):
                            resp = b'---object does not have attribute requested'
                            conn.sendall(resp)
                            continue
                        
                        # error handling for wrong args
                        try:
                            result = getattr(obj, method)(*args, **kwargs)
                        except Exception as e:
                            print('error while calling', method)
                            result = '---' + str(e)

                        resp = str(result).encode()
                    else:
                        resp = b'---invalid message'


                    conn.sendall(resp) 








    
