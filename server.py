#server
import socket
import threading
from classes import *
def main():
    def clientHandel(conn,addr):
        print(f'{addr} connected')
        while True:
            messege = reciveMessege(conn)
            if messege == DISCONNECT:
                print(f'{addr} disconnected')
                break
            else:...
    def reciveMessege(conn):
        messege_len = conn.recv(HEADER).decode(FORMAT)
        if messege_len:
            messege_len = int(messege_len)
            messege = conn.recv(messege_len).decode(FORMAT)
            return messege
        return None
    def sendMessege(msg,conn):
        messege = msg.encode(FORMAT)
        messege_len = len(messege)
        messege_len = str(messege_len).encode(FORMAT)
        messege_len += b' ' * (HEADER - len(messege_len))
        conn.send(messege_len)
        conn.send(messege)
    PORT = 5000
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER,PORT)
    HEADER = 64
    FORMAT = 'utf-8'
    DISCONNECT = '!disc!!'
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(SERVER)
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=clientHandel,args=(conn,addr))
        thread.start()

if __name__ == '__main__':
    main()