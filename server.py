import socket
import threading
from _CaesarCipher import CaesarCipher

users = []


def deleteClient(client):
    users.remove(client)
    

def auto_eco(client, msg):
    for x in users:
        try:
            encrypted = CaesarCipher(msg.decode(), "E", 3).encrypt()
            x.send(encrypted.encode())
        except Exception as err:
            deleteClient(x)

def receber_msg(client):
    try:
        while True:
            msg = client.recv(2048).decode("utf-8")
            decrypt = CaesarCipher(msg, "D", 3).decrypt()
            auto_eco(client, decrypt.encode("utf-8"))
    except Exception as err:
        print(err)
        print("Usuario Desconectado")


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "localhost"
    port = 5555

    s.bind((host,port))
    s.listen(10)
    while True:
        client, addres = s.accept()
        users.append(client)
        print("user:", addres)

        t = threading.Thread(target=receber_msg, args=[client])
        t.start()


main()