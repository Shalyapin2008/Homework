import socket

sock = socket.socket()
try:
	sock.connect(('localhost', 9090))
	print("Подключение прошло успешно, введите сообщение")
	msg=""
	msg=input()
	print("отправка данных")
	try:
		msg=""
		msg=input()
		while msg!="stop":
			sock.send(msg.encode())
			data = sock.recv(1024)
			print("данные отправлены")			
			msg=input()
			pass
		 
	except:
		print("данные не отправлены")

	sock.close()
	data = sock.recv(1024)

	print(data)
except:
	print("подключение оборвалось")
	sock.close()
	


