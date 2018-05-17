# client
if __name__ == '__main__':
    import socket
    import sys

    if len(sys.argv) != 3:
        print("should have a host and port as argument...")
        sys.exit(1)

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])

    with socket.socket() as s: # close after finished
        print("stablishing connection to", HOST, PORT)
        # stablish connection
        try:
            s.connect((HOST, PORT))

            while True:
                cmd = input("command:")

                msg = ""

                if cmd == "i":
                    print("incrementing...")
                    msg = b'i'
                elif cmd == "r":
                    print("reseting...")
                    msg = b'r'
                elif cmd == "d":
                    print("decrementing...")
                    msg = b'd'
                elif cmd == "e":
                    print("exiting programm\nclosing connection")
                    break
                else:
                    print("invalid command")
                    continue

                # attempt to send all data
                s.sendall(msg)
                # receive response in buffered 1024 bytes
                data = s.recv(16)
                response = int.from_bytes(data, byteorder=sys.byteorder, signed=True)
                print('received:', response)
        except:
            print("unable to connect to", HOST, PORT)
       
        