import socket

sock = socket.socket()
sock.bind(('', 9090))
print("сервер запущен")
sock.listen(1)

command=''
while command!="stop":
	
	sock.listen(1)
	print("ожидание подключ")
	conn, addr = sock.accept()

	print ('соединение с:', addr)


	
	counter=0

	while True:
	    msg=''
	    data = conn.recv(1024)
	    if not data:
	        break
	    msg+=data.decode()
	    conn.send(data.upper())
	    print(msg)
	print("продолжить или отключить сервер?")
	command=input()
conn.close()

"""
conn, addr = sock.accept()

print ('соединение с:', addr)


msg=' '
counter=0

while True:
    data = conn.recv(1024)
    if not data:
        break
    msg+=data.decode()
    conn.send(data.upper())
    print(msg)
conn.close()
"""

"""	
while counter!=10:
	pass
	while msg[-1]!=".":
		data = conn.recv(1024)
		if not data:
			break 
		
		msg+=data.decode()
		conn.send(data.upper())
		print(msg)
	counter+=1

conn.close()
"""