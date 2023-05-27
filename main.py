"""
Nombre: programa principal
Descripción: Este será el programa principal de nuestra practica de desarrollo del software.
Precauciones: :D
"""

import string
from UC3MCare import VaccineManager
#from UC3MCare import VaccineRequest

#GLOBAL VARIABLES
LETTERS = string.ascii_letters + string.punctuation + string.digits
SHIFT = 3


def encode(word):
    """Codifica"""
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (LETTERS.index(letter) + SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[x]
    return encoded

def decode(word):
    """Decodifica"""
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (LETTERS.index(letter) - SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[x]
    return encoded

def main():
    """Funcion principal"""
    mng = VaccineManager()
    res = mng.readaccessrequestfromJson("test.json")
    strRes = res.__str__()
    print(strRes)
    encodeRes = encode(strRes)
    print("Encoded Res "+ encodeRes)
    decodeRes = decode(encodeRes)
    print("Decoded Res: " + decodeRes)


if __name__ == "__main__":
    main()
