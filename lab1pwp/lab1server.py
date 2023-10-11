import socket
import time

host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

server_socket.listen(1)
print(f"Сервер: {host}:{port}")

client_socket, client_address = server_socket.accept()
print(f"{client_address} приєднався")

data = client_socket.recv(1024)
size = int(client_socket.recv(1024).decode('utf-8'))
time.sleep(5)

if size == len(data):

    print(
        f"Отримано: {data.decode('utf-8')} ({time.strftime('%Y-%m-%d %H:%M:%S')})")
    client_socket.sendall(("Ви надіслали: "+data).encode('utf-8'))
else:
    print(f"Дані пошкоджено")
    client_socket.sendall(("Дані пошкоджено: "+data).encode('utf-8'))


client_socket.close()
server_socket.close()
