import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 1080))
message = ''

while True:
    msg = s.recv(1)
    if len(msg) <= 0:
        break
    else:
        message += msg.decode("utf-8")

print(message)