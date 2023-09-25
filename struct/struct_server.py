import socket
import struct
print("Servidor")
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(("",1234))
    while True:
        msg, addr= s.recvfrom(1024)
        try:
            texto=struct.unpack('<H6s',msg)[1]
            numero=struct.unpack('<H6s',msg)[0]
            print(numero)
            print(texto.decode().strip())
        except: 
            print("fua nano se lio parda")
            s.close()