import socket
#socket tipo ipv4 y UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    print("Servidor ...")
    s.bind(("",1234))
    msg, addr= s.recvfrom(1024)
print(addr[0])