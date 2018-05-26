# decorator for constant key determination
def constant_key(k):
    def dec(original_func):

        def wrapper(*args, **kwargs):
            return original_func(k, *args, **kwargs)
        
        return wrapper
    return dec


# get an specific object from a specified 
# server address
def lookup(addr, name):
    # stablish connection to remote server
    import socket
    import pickle

    with socket.socket() as s:
        s.connect(addr)

        msg = name.encode()

        s.sendall(msg)

        data = s.recv(1024)

        if not data: 
            print("server didn´t answer")
            return

        resp = data.decode(errors='ignore')

        if resp.startswith('---'):
            print("object not found")
            return
        
        obj = pickle.loads(data)

        obj_dir = dir(obj)

        for key in list(obj_dir):
            method = getattr(obj, key)
            if callable(method) and not key.startswith('__'):
                
                # reimplements the methods for remote method invocation
                # uses a decorator so that everytime the function is defined, 
                # it doesn't change all the previous definitions
                @constant_key(key)
                def dynamic_method(k, *args, **kwargs):

                    # open connection and send the corresponding commands
                    import socket

                    with socket.socket() as sock:
                        sock.connect(addr)
                        cmd = str(name) + "-" + str(args) + "-" + str(kwargs) + "-" + k
                        sock.sendall(cmd.encode())

                        data = sock.recv(1024)

                        result = data.decode(errors='ignore')

                        return result

                setattr(obj, key, dynamic_method)

        return obj