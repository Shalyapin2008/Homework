import socket
import datetime


file = 'logs.txt'
logs=[]



sock = socket.socket()


sock.bind(('', 9090))

print("***Сервер запущен***")
logs.append(str(datetime.datetime.now())+" запущен сервер")

sock.listen(1)



command=''
while command!="stop":
	
	sock.listen(1)
	print("***Ожидание подключения***")
	conn, addr = sock.accept()
	logs.append(str(datetime.datetime.now())+"Установлено соединение с "+addr[0])
	print ('***Установлено соединение с:', addr,'***')

	while True:
	    data = conn.recv(1024)
	    msg=''
	    if not data:
	        break
	    msg+=data.decode() 
	    conn.send(data.upper())
	    print(msg)
	logs.append(str(datetime.datetime.now())+" пользователь "+ addr[0]+" отключился")
	print("***Пользователь "+addr[0]+" отключился***")
	print("***Продолжить или отключить сервер?***")
	command=input()
logs.append(str(datetime.datetime.now())+" сервер завершает работу")
logs.append("---"*20)

try:
	f=open(file,'a')
	for i in logs:
		f.write(i+'\n')
except:
	f=open(file,'w')
	for i in logs:
		f.write(i+'\n')
f.close()
conn.close()
