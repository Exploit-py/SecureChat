import socket
import threading
from _CaesarCipher import CaesarCipher


def enviar_msg(client, username):
    try:
        while True:
            msg = input("")
            print("")
            encrypted_msg = CaesarCipher(msg, "E", 3).encrypt()
            encrypted_user = CaesarCipher(username, "E", 3).encrypt()

            client.send(f'{encrypted_user}: {encrypted_msg}\n'.encode("utf-8"))
    except Exception as err:
        print(err)


def receber_msgs(client):
    try:
        while True:
            msg = client.recv(2048).decode("utf-8")
            decrypt = CaesarCipher(msg, "D", 3).decrypt()
            print(decrypt)
    except Exception as err:
        print(err)


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "localhost"
    port = 5555
    s.connect((host,port))
    username = input("username: ")
    
    t = threading.Thread(target=enviar_msg, args=[s, username])
    t2 = threading.Thread(target=receber_msgs, args=[s])
    t.start()
    t2.start()


main()
