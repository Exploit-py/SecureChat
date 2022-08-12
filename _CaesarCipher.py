import platform

from string import ascii_letters
from os import system


options = {"E": "Encriptar", "D": "Decriptar"}


def ClearTerminal():
    if platform.system() == "Windows":
        return system("cls")
    else:
        return system("clear")


def menu():
    ClearTerminal()
    print(f"{'-'*10}Ceasar Cipher{'-'*10}")
    for x,y in options.items():
        print(f"[{x}] - {y}")


class CaesarCipher():
    def __init__(self, text: str, option: str, rotation = 3) -> dict:
        self.text = text
        self.option = option
        self.rotation = rotation
        self.alphabet = ascii_letters
    
    def cipher(self):
        global options
        if self.option == "E":
            return self.encrypt()
        else:
            return self.decrypt()

    def encrypt(self) -> str:
        encrypted_string = ""
        for x in self.text:
            try:
                index = self.alphabet.index(x)
                encrypted_string += self.alphabet[index + self.rotation]
            except:
                encrypted_string += x
        return encrypted_string

    def decrypt(self) -> str:
        decrypted_string = ""
        for x in self.text:
            try:
                index = self.alphabet.index(x)
                decrypted_string += self.alphabet[index - self.rotation]
            except:
                decrypted_string += x
        return decrypted_string


if __name__=="__main__":
    while True:
        menu()
        option = input("O que deseja fazer?: ").upper()[0]
        ClearTerminal()
        try:
            print(f"{'-'*10}{options[option]}{'-'*10}")
            text = input(f"Digite o que deseja {options[option]}: ")
            rotate = int(input("Qual a rotação?: "))
            obj = CaesarCipher(text, option, rotate)
            print(f"\n- String: {obj.cipher()}")

        except KeyError:
            print(f'\nERROR: Opção Inválida')
        
        reset = input("\nDigitar outra coisa?[Y]/[n]: ").upper()
        if reset == "N":
            break
