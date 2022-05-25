import socket
import threading


def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'nickname':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            client.close()
            print('Server is down...')
            break


def send_message():
    while True:
        current_client_msg = input()
        message = f'{nickname}: {current_client_msg}'
        client.send(message.encode('utf-8'))


if __name__ == '__main__':
    nickname = input('Welcome to the chat! Enter your nickname: ')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 1239))

    threading.Thread(target=receive).start()
    threading.Thread(target=send_message).start()


