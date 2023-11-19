import socket
while True :
	s = input(">>>")
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock :
		sock.connect((socket.gethostbyname(socket.gethostname()), 8549))
		sock.send(s.encode())
		data = sock.recv(1024).decode()
		print(data)