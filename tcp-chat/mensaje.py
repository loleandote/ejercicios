import socket, sys, argparse
def cliente():
    print("cliente iniciado...")
    with  socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        mensaje ="hola"
        while mensaje != "exit":
            s.sendto(mensaje.encode(),("localhost",1234))
            print("mensaje enviado")
            msg, addr= s.recvfrom(1024)
            print(msg.decode())

    sys.exit(0)
def servidor():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    BUFFER_SIZE = 20  # Normally 1024, but we want fast response
    print("hoal")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connection address:'), addr
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print("received data:"), data
        conn.send(data)  # echo
    conn.close()

parser = argparse.ArgumentParser()
parser.add_argument(
    "-m","--mode",
    type=str,
    default="server",
    required=False
)
args=parser.parse_args()
#primer argumento que se recive a la hora de ejecutar el programa
mode= sys.argv[1] if len(sys.argv) >1  else 'server'
servidor() if args.mode== "server" else cliente()