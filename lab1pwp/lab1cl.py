import socket
host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host, port))


message = input("Введіть текст: ")

client_socket.sendall(message.encode('utf-8'))
client_socket.close()
# asd
