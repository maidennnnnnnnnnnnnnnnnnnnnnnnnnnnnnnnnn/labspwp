import socket
import threading

host = '127.0.0.1'
port = 55555
print(f"Сервер: {host}:{port}")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast("{} покинув нас".format(nickname).encode('utf-8'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print("{} приєднався".format(str(address)))
        client.send('Ім\'я'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        print("{}".format(nickname))
        broadcast("{} приєднався".format(nickname).encode('utf-8'))
        client.send(f"Приєднано до {host}:{port}".encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
