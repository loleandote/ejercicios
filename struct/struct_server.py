import socket
#def servidor():
#primer argumento que se recive a la hora de ejecutar el programa
#mode=sys.argv[1]
#socket tipo ipv4 y UDP
print("Servidor")
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
#socket tipo ipvv6 y TCP
#s= socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    s.bind(("",1234))
while True:
    msg, addr= s.recvfrom(1024)
    try:
        numerobytes=msg[:16]
        numero= numerobytes.decode()
        texto=msg[16:]
        print(numero)
        #print(msg.decode('ascii'))
        print(texto.decode().strip())
    except: 
        print("fua nano se lio parda")
#    return True
#servidor()