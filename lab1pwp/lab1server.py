import socket
import time

host = '127.0.0.1'
port = 43287

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

server_socket.listen(1)
print(f"Сервер: {host}:{port}")
while True:
    client_socket, client_address = server_socket.accept()
    print(f"{client_address} приєднався")

    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if data.lower() == "stop":
            break
        size = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        # time.sleep(5)

        if int(size) == int(len(data)):
            print(
                f"Отримано: {data} ({time.strftime('%Y-%m-%d %H:%M:%S')})")
            client_socket.send(("Ви надіслали: "+data).encode('utf-8'))
        else:
            print(f"Дані пошкоджено")
            client_socket.send(("Дані пошкоджено: "+data).encode('utf-8'))

    client_socket.close()
server_socket.close()
