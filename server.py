import socket

sock = socket.socket()
sock.bind(('', 9090))
print("сервер запущен")
sock.listen(1)
print("ожидание подключ")
conn, addr = sock.accept()

print ('connected with:', addr)


msg=''
while True:
    data = conn.recv(1024)
    if not data:
        break
    msg+=data.decode()
    conn.send(data.upper())

print(msg)

conn.close()