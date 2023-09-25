# ip 172.19.196.163
#puerto=4080
import socket as coso
def cliente():
    texto =" hola"
    with  coso.socket(coso.AF_INET, coso.SOCK_DGRAM) as s:
        s.sendto(texto.encode('utf-8'),("localhost",1234))
    return True
if __name__ == "__main__":
    cliente()