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
                    else:
                        # if the request has multiple arguments
                        # then it means it's a method call

                        from ast import literal_eval

                        # the first parameter must be a dictionary key
                        if not req_list[0] in self.object_dictionary:
                            resp = b'---object not found'
                            conn.sendall(resp)
                            continue
                        
                        # the arguments must be a valid tuple and a valid dictionary
                        # try:

                        #     args = literal_eval(req_list[1])
                        #     kwargs = literal_eval(req_list[2])

                        #     with self.object_dictionary[req_list[0]] as obj:

                        #         if not hasattr(obj, req_list[3]):
                        #             resp = b'---object does not have attribute requested'
                        #             conn.sendall(resp)
                        #             continue
                                
                        #         result = getattr(obj, req_list[3])(*args, **kwargs)
                        #         resp = str(result).encode()

                        # except Exception as e:
                        #     print('Error parsing arguments', e)
                        #     resp = b'---invalid args or kwargs'

                        args = literal_eval(req_list[1])
                        kwargs = literal_eval(req_list[2])

                        obj = self.object_dictionary[req_list[0]]

                        if not hasattr(obj, req_list[3]):
                            resp = b'---object does not have attribute requested'
                            conn.sendall(resp)
                            continue
                        
                        result = getattr(obj, req_list[3])(*args, **kwargs)
                        resp = str(result).encode()


                    conn.sendall(resp) 








    
