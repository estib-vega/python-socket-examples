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

        return obj