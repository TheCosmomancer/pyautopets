#client
import socket
import pygame
def main():
    # PORT = 5000
    # FORMAT = 'utf-8'
    # SERVER = "127.0.0.2"
    # ADDR = (SERVER,PORT)
    # HEADER = 64
    # DISCONNECT = '!disc!!'
    # client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # client.connect(ADDR)
    # def sendMessege(msg):
    #     messege = msg.encode(FORMAT)
    #     messege_len = len(messege)
    #     messege_len = str(messege_len).encode(FORMAT)
    #     messege_len += b' ' * (HEADER - len(messege_len))
    #     client.send(messege_len)
    #     client.send(messege)
    # def reciveMessege():
    #     messege = None
    #     while messege == None:
    #         messege_len = client.recv(HEADER).decode(FORMAT)
    #         if messege_len:
    #             messege_len = int(messege_len)
    #             messege = client.recv(messege_len).decode(FORMAT)
    #             return messege
    screen = 'login'
    pygame.init()
    screen = pygame.display.set_mode([500, 500])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
        pygame.display.flip()
if __name__ == '__main__':
    main()
    pygame.quit()