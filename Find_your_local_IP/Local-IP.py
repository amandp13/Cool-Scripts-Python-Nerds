import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.1.1.1", 80))  # Any DNS Server
    myIp = s.getsockname()[0]
    s.close()
    print(myIp)


if __name__ == "__main__":
    main()