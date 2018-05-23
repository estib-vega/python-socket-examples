# client
if __name__ == '__main__':
    import sys
    from client_counter import ClientCounter


    if len(sys.argv) != 3:
        print("should have a host and port as argument...")
        sys.exit(1)

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])

    my_c = ClientCounter(HOST, PORT)

    while True:
        cmd = input('command:')

        val = -404

        # decode the command
        if cmd == "i":
            # increment
            val = my_c.increment()
        elif cmd == "d":
            #decrement
            val = my_c.decrement()
        elif cmd == "r":
            val = my_c.reset()
        elif len(cmd.split()) == 2:
            cmd_list = cmd.split()
            if cmd_list[0] == "s":
                try:
                    v = int(cmd_list[1])
                    val = my_c.set_value(v)
                except ValueError:
                    print("invalid value:", cmd_list[1])
            else:
                print('invalid commands:', cmd)
        elif cmd == "e":
            print("exiting programm...")
            sys.exit(1)
        else:
            print('invalid command:', cmd)

        print("result:", val)


    
       
        