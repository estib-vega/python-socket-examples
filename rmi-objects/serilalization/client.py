def main():
    from remote_client import lookup
    import sys

    if len(sys.argv) != 3:
        print("should have a host and port as argument...")
        sys.exit(1)

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])

    my_c = lookup((HOST, PORT), 'Counter')

    if not my_c:
        sys.exit(1)

    while True:
        cmd = input('command:')

        val = None

        if cmd == "i":
            # increment
            val = my_c.increment()
        elif cmd == "d":
            #decrement
            val = my_c.decrement()
        elif cmd == "r":
            # reset
            val = my_c.reset()
        elif len(cmd.split()) == 2:
            # two arguments
            cmd_list = cmd.split()

            if cmd_list[0] == "s":
                # set
                try:
                    # parse value
                    v = int(cmd_list[1])
                    val = my_c.set_value(v)
                except ValueError:
                    print("invalid value:", cmd_list[1])
            else:
                print('invalid commands:', cmd)
        elif cmd == "e":
            # exit
            print("exiting programm...")
            sys.exit(1)
        else:
            # invalid
            print('invalid command:', cmd)

        print("result:", val)




if __name__ == '__main__':
    main()