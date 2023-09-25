import socket as coso
import struct
import string
import random
def cliente():
    texto =""
    letras= random.randint(0,10)
    i=0
    print(letras)
    while i<letras:
        texto+=random.choice(string.ascii_letters)
        i+=1
    print(texto)
    bites = texto.encode()
    tamano = len(bites)
    with  coso.socket(coso.AF_INET, coso.SOCK_DGRAM) as s:
        s.sendto(struct.pack('<H6s',tamano,texto.encode()),("localhost",1234))
    return True
cliente()