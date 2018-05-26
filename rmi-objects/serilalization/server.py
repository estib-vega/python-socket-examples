def main():
    import sys
    from remote_server import RemoteServer
    from counter import Counter
    
    if len(sys.argv) != 2:
        print("should have a port as argument...")
        sys.exit(1)

    PORT = int(sys.argv[1])

    r_s = RemoteServer(PORT)
    c = Counter()

    r_s.bind_object(c, 'Counter')
    r_s.run()

if __name__ == '__main__':
    main()


