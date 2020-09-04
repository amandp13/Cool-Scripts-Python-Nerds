import socket


Header = 64
Port = 5050
# Server = '192.168.0.107' # Will Change Respect To Computers..
Server = socket.gethostbyname(socket.gethostname())
Addr = (Server, Port)
Format = 'utf-8'
Disconnect_msg = '!DISCONNECT'


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(Addr)

end = True


def send(msg):
    message = msg.encode(Format)
    msg_len = str(len(message)).encode(Format)
    msg_len += b' ' * (Header - len(msg_len))
    client.send(msg_len)
    client.send(message)
    try:
        return_msg = client.recv(1024).decode(Format)
        print(return_msg)
        if return_msg == 'Msg_received':
            print('\t Received')
        else:
            print(f'[Warning]')
    except Exception as e:
        print(f'Warning : {e} occurred')


while end:
    mssg = input('Enter : ')
    send(mssg)
    opt = input('Do U Want To Exit : ')
    if opt == 'Y' or opt == 'y' or opt == 'Yes' or opt == 'YES': # Worst way !
        send(Disconnect_msg)
        break

print('Exiting')





