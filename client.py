def cmd_interpreter(sys, my_c):
    method_list = list(dir(my_c))
    callables = []
    print('avilible methods:')

    # save the callable methods so they can be 
    # dynamically called upon
    for m in method_list:
        if not str(m).startswith('__'):
            method = getattr(my_c, m)
            if callable(method):
                callables.append(m)
                # show them
                print(str(len(callables) - 1), 'for', str(m))
                
    print('e for exiting programm')
    
    # command loop
    while True:
        cmd = input('command: ')

        if cmd == "e":
            # exit
            print("exiting programm...")
            sys.exit(1)
        else:
            try:
                c_list = list(cmd.split())
                if len(c_list) == 1:
                    i = int(cmd)
                    val = getattr(my_c, callables[i])()
                else:
                    i = int(c_list[0])
                    args = tuple(c_list[1::])
                    val = getattr(my_c, callables[i])(*args)

                print("result:", val)
                
            except:
                print('could not parse command\ninvalid command')


def main():
    from remote_client import lookup
    import sys

    if len(sys.argv) != 3:
        print("should have a host and port as argument...")
        sys.exit(1)

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])

    # get object to be looked for
    name = input('object name to be looked for: ')

    my_c = lookup((HOST, PORT), name)

    if not my_c:
        sys.exit(1)

    cmd_interpreter(sys, my_c)



if __name__ == '__main__':
    main()