#server
import socket
import threading
from classes import *
import uuid
def main():
    def clientHandel(conn,addr):
        print(f'{addr} connected')
        while True:
            messege = reciveMessege(conn)
            if messege == DISCONNECT:
                print(f'{addr} disconnected')
                break
            elif messege == 'getenemy':
                while True:
                    allready = True
                    for player in LOBBIES[mylobby]:
                        if player.day != myplayer.day:
                            allready = False
                    if allready:
                        break
                while True:
                    enemy = random.choice(LOBBIES[mylobby])
                    if enemy != myplayer:
                        break
                sendMessege(obj2str(enemy),conn)
            elif messege == 'newlobby':
                while True:
                    newuuid = str(uuid.uuid4())
                    if newuuid not in LOBBIES.keys():
                        sendMessege(newuuid,conn)
                        LOBBIES[newuuid] = []
                        mockplayer = Player(warband = [None,None,None,None,None],shop = [None,None,None,None,None,None],day = 0,coins = 10,lives = 4,wins = 0)
                        mockplayer.uuid = 'foo'
                        break
            else:
                messege = messege.split('¶')
                if messege[0] == 'saveplayer':
                    myplayer = str2obj(messege[1])
                elif messege[0] == 'connectlobby':
                    if messege[1] in LOBBIES.keys():
                        while True:
                            playeruuid = str(uuid.uuid4())
                            uniqe = True
                            for player in LOBBIES[messege[1]]:
                                if player.uuid == playeruuid:
                                    uniqe = False
                            if uniqe == True:
                                break
                        myplayer = Player(warband = [None,None,None,None,None],shop = [None,None,None,None,None,None],day = 0,coins = 10,lives = 4,wins = 0)
                        myplayer.uuid = playeruuid
                        mylobby = messege[1]
                        LOBBIES[mylobby].append(myplayer)
                        sendMessege('¶',conn)
                    else:
                        sendMessege('not found')
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
    LOBBIES = {}
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