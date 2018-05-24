from counter_interface import RemoteCounter
import socket
import sys

class ClientCounter (RemoteCounter):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def increment(self):
        # send command for increment
        return self.send_command('i')

    def decrement(self):
        # send command for decrement
        return self.send_command('d')
    
    def set_value(self, value):
        # send command for set value
        return self.send_command('s {}'.format(value))
    
    def reset(self):
        # send command for reset
        return self.send_command('r')

    # conncetion and command
    def send_command(self, cmd):
        with socket.socket() as s: # close after finished
            print("stablishing connection to", self.host, self.port)
            # stablish connection
            try:
                s.connect((self.host, self.port))
                
                msg = cmd.encode()

                s.sendall(msg)

                data = s.recv(1024)

                if not data: 
                    print("server didn´t answer")
                    return -404

                res = int.from_bytes(data, sys.byteorder, signed=True)
                return res

            except Exception as e:
                print(e)
                print("unable to connect to", self.host, self.port)

    