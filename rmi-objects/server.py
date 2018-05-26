
def main():
    import socket
    import sys
    from counter import Counter

    c = Counter()


    if len(sys.argv) != 2:
        print("should have a port as argument...")
        sys.exit(1)

    HOST = 'localhost'
    PORT = int(sys.argv[1])

    with socket.socket() as sock:
        sock.bind((HOST, PORT)) 

        sock.listen(2)

        while True:
            
            print("listening in localhost at port", PORT, "...")

            try:
                conn, addr = sock.accept()
            except:
                print("\nended programm")
                sock.close()
                sys.exit(1)

            print("initiated connection from:", addr)
            with conn:
                while True:
                    
                    try:
                        data = conn.recv(1024)
                    except:
                        print("\nended programm")
                        sock.close()
                        sys.exit(1)
                    
                    cmd = data.decode()
                    res = -1

                    if not data: break 

                     # decode the command
                    if cmd == "i":
                        # increment
                        res = c.increment()
                    elif cmd == "d":
                        #decrement
                        res = c.decrement()
                    elif cmd == "r":
                        res = c.reset()
                    elif len(cmd.split()) == 2:
                        cmd_list = cmd.split()
                        if cmd_list[0] == "s":
                            res = c.set_value(int(cmd_list[1]))
                        else:
                            print('invalid value')
                    else:
                        print('invalid command:', cmd)

                    response = res.to_bytes(1024, sys.byteorder, signed=True)
                    
                    conn.sendall(response)


if __name__ == '__main__':
    main()