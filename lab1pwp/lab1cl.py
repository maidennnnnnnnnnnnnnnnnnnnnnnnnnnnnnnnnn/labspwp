import socket

host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

message = input("Введіть текст: ")

client_socket.sendall(message.encode('utf-8'))
client_socket.sendall(str(len(message)).encode('utf-8'))
data = client_socket.recv(1024)
print(data)
client_socket.close()
