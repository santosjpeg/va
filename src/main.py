from server import Server

def main():
    s = Server()

    if s.get_is_running() == False:
        s.start()

if __name__ == '__main__':
    main()
