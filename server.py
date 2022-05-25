import socket
import threading
from datetime import datetime


def send_message(connections_dict, message):
    if len(connections_dict) > 0:
        for client in connections_dict.values():
            client.send(message)


def get_key(client):
    for nickname, value in clients.items():
        if value == client:
            return nickname


def check_if_the_nickname_already_exist(nickname):
    pass


def receive(client):
    while True:
        try:
            message = client.recv(1024)
            for client in clients.values():
                client.send(message)
        except:
            nickname = get_key(client)
            client.close()
            del clients[nickname]
            print(f'{nickname} left the server at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}!')
            message = f'{nickname} left the chat!'.encode('utf-8')
            send_message(clients, message)
            break


clients = {}


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 1239))
    server.listen()

    print('Server is listening...')

    while True:
        client, address = server.accept()
        client.send('nickname'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        clients[nickname] = client

        print(f'{nickname} join the server at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}!')
        message = f'{nickname} join the chat!'.encode('utf-8')
        send_message(clients, message)

        threading.Thread(target=receive, args=(client, )).start()


if __name__ == '__main__':
    main()