import socket
import threading
import time

Header = 64
Port = 5050
# server = '192.168.0.107' # HardCoded
Server = socket.gethostbyname(socket.gethostname())
# print(f'debug : Server ')
Addr = (Server, Port)
Format = 'utf-8'
Disconnect_msg = '!DISCONNECT'

# bind
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(Addr)


def start():
    """ Starts The Server !"""
    print(f'[Starting] server {Server} @ {time.time()}')
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        print(f'[Active Connections] : {threading.activeCount()}') # thread => one running current program \n new thread starts
        thread.start()


def handle_client(conn, addr):
    """ Handle Client Connection !"""
    print(f'\n[New Connection] : {addr} connected @{time.time()}')

    connected = True
    while connected:
        msg_len = conn.recv(Header).decode(Format)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(Format)
            if msg == Disconnect_msg:
                connected = False
            print(f'{addr} >> {msg}')
            conn.send('Msg_received'.encode(Format))
    
    conn.send('!DISCONNECT'.encode(Format))
    print(f'[Connection Closed] : {addr} @ {time.time()}\n')
    conn.close()


start()
# Eof
