import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 1080))
s.listen()

message = "Hello World"
message = bytes(message, "utf-8")

while True:
    clt, adr = s.accept()
    clt.send(message)
    clt.close()