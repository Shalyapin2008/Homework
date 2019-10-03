import socket

sock = socket.socket()
try:
	sock.connect(('localhost', 9090))
	print("Подключение прошло успешно, введите сообщение:")
	msg=""
	msg=input()
	sock.send(msg.encode())

	data = sock.recv(1024)

	print(data)

	sock.close()
except:
	print("подключение не прошло")
	sock.close()
	


