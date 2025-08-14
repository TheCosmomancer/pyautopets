#client
import socket
import pygame
import tkinter as tk
from classes import *
import uuid
import random
import time
def main():
    PORT = 5000
    FORMAT = 'utf-8'
    SERVER = "127.0.0.2"
    ADDR = (SERVER,PORT)
    HEADER = 64
    DISCONNECT = '!disc!!'
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def sendMessege(msg):
        messege = msg.encode(FORMAT)
        messege_len = len(messege)
        messege_len = str(messege_len).encode(FORMAT)
        messege_len += b' ' * (HEADER - len(messege_len))
        client.send(messege_len)
        client.send(messege)
    def reciveMessege():
        messege = None
        while messege == None:
            messege_len = client.recv(HEADER).decode(FORMAT)
            if messege_len:
                messege_len = int(messege_len)
                messege = client.recv(messege_len).decode(FORMAT)
                return messege
    def findkeytoshow (n):
        if n == 0:
            return 'Q'
        elif n == 1:
            return 'W'
        elif n == 2:
            return 'E'
        elif n == 3:
            return 'A'
        elif n == 4:
            return 'S'
        elif n == 5:
            return 'D'
    def playpygame (mode,player):
        pygame.init()
        Honey = pygame.image.load("./assets/Honey.png")
        Apple = pygame.image.load("./assets/Apple.png")
        SleepingPill = pygame.image.load("./assets/Sleeping Pill.png")
        MeatBone = pygame.image.load("./assets/Meat Bone.png")
        Garlic = pygame.image.load("./assets/Garlic.png")
        Salad = pygame.image.load("./assets/Salad.png")
        Pear = pygame.image.load("./assets/Pear.png")
        Chili = pygame.image.load("./assets/Chili.png")
        Chocolate = pygame.image.load("./assets/Chocolate.png")
        Sushi = pygame.image.load("./assets/Sushi.png")
        Steak = pygame.image.load("./assets/Steak.png")
        Melon = pygame.image.load("./assets/Melon.png")
        Pizza = pygame.image.load("./assets/Pizza.png")
        Peanut = pygame.image.load("./assets/Peanut.svg")
        Cricket = pygame.image.load("./assets/Cricket.png")
        Pig = pygame.image.load("./assets/Pig.png")
        Duck = pygame.image.load("./assets/Duck.png")
        Beaver = pygame.image.load("./assets/Beaver.png")
        Crab = pygame.image.load("./assets/Crab.png")
        Peacock = pygame.image.load("./assets/Peacock.png")
        Flamingo = pygame.image.load("./assets/Flamingo.png")
        Spider = pygame.image.load("./assets/Spider.png")
        Sheep = pygame.image.load("./assets/Sheep.png")
        Dodo = pygame.image.load("./assets/Dodo.png")
        Ox = pygame.image.load("./assets/Ox.png")
        Camel = pygame.image.load("./assets/Camel.png")
        Turtle = pygame.image.load("./assets/Turtle.png")
        Deer = pygame.image.load("./assets/Deer.png")
        Parrot = pygame.image.load("./assets/Parrot.png")
        Skunk = pygame.image.load("./assets/Skunk.png")
        Armadillo = pygame.image.load("./assets/Armadillo.png")
        Rooster = pygame.image.load("./assets/Rooster.png")
        Shark = pygame.image.load("./assets/Shark.png")
        Scorpion = pygame.image.load("./assets/Scorpion.png")
        Mammoth = pygame.image.load("./assets/Mammoth.png")
        Dragon = pygame.image.load("./assets/Dragon.png")
        Boar = pygame.image.load("./assets/Boar.png")
        Snake = pygame.image.load("./assets/Snake.png")
        Bus = pygame.image.load("./assets/Bus.png")
        Chicken = pygame.image.load("./assets/Chicken.png")
        Bee = pygame.image.load("./assets/Bee.png")
        Sheeplet = pygame.image.load("./assets/Sheeplet.png")
        Cricklet = pygame.image.load("./assets/Cricklet.png")
        Giraffe = pygame.image.load("./assets/Giraffe.png")
        def findanimaltoshow(name):
            if name == 'Giraffe':
                return Giraffe
            elif name == 'Cricklet':
                return Cricklet
            elif name == 'Sheeplet':
                return Sheeplet
            elif name == 'Bee':
                return Bee
            elif name == 'Chicken':
                return Chicken
            elif name == 'Bus':
                return Bus
            elif name == 'Cricket':
                return Cricket
            elif name == 'Pig':
                return Pig
            elif name == 'Duck':
                return Duck
            elif name == 'Beaver':
                return Beaver
            elif name == 'Crab':
                return Crab
            elif name == 'Peacock':
                return Peacock
            elif name == 'Flamingo':
                return Flamingo
            elif name == 'Spider':
                return Spider
            elif name == 'Sheep':
                return Sheep
            elif name == 'Dodo':
                return Dodo
            elif name == 'Ox':
                return Ox
            elif name == 'Camel':
                return Camel
            elif name == 'Turtle':
                return Turtle
            elif name == 'Deer':
                return Deer
            elif name == 'Parrot':
                return Parrot
            elif name == 'Skunk':
                return Skunk
            elif name == 'Armadillo':
                return Armadillo
            elif name == 'Rooster':
                return Rooster
            elif name == 'Shark':
                return Shark
            elif name == 'Scorpion':
                return Scorpion
            elif name == 'Mammoth':
                return Mammoth
            elif name == 'Dragon':
                return Dragon
            elif name == 'Boar':
                return Boar
            elif name == 'Snake':
                return Snake
            else:
                return None
        def findfoodtoshow(name):
            if name == 'Peanut':
                return Peanut
            elif name == 'Honey':
                return Honey
            elif name == 'Apple':
                return Apple
            elif name == 'Sleeping Pill':
                return SleepingPill
            elif name == 'Meat Bone':
                return MeatBone
            elif name == 'Garlic':
                return Garlic
            elif name == 'Salad':
                return Salad
            elif name == 'Pear':
                return Pear
            elif name == 'Chili':
                return Chili
            elif name == 'Chocolate':
                return Chocolate
            elif name == 'Sushi':
                return Sushi
            elif name == 'Steak':
                return Steak
            elif name == 'Melon':
                return Melon
            elif name == 'Pizza':
                return Pizza
            elif name == 'Peanut':
                return Peanut
            else:
                return None
        wallpaper = pygame.transform.scale(pygame.image.load("./assets/wallhaven-jxrrmp_3840x2160.png"), (1600, 900))
        COIN = pygame.transform.scale(pygame.image.load("./assets/coin.svg"), (100, 100))
        LIVES = pygame.transform.scale(pygame.image.load("./assets/Lives.png"), (100, 100))
        WINS = pygame.transform.scale(pygame.image.load("./assets/Wins.png"), (100, 100))
        NEXT = pygame.transform.scale(pygame.image.load("./assets/next.svg"), (100, 100))
        REROLL = pygame.transform.scale(pygame.image.load("./assets/reroll.svg"), (100, 100))
        SELL = pygame.transform.scale(pygame.image.load("./assets/sell.svg"), (70, 70.))
        FREEZE = pygame.transform.scale(pygame.image.load("./assets/freeze.svg"), (70, 70))
        smallfont = pygame.font.SysFont('Arial', 20)
        font = pygame.font.SysFont('Arial', 36)
        bigfont = pygame.font.SysFont('Arial', 72)
        screen = pygame.display.set_mode((1600, 900))
        running = True
        held = False
        gamephase = 'newday'
        COIN_COUNT = bigfont.render(f'{player.coins}', False, (0, 0, 0))
        outcome = None
        inp = [None,None]
        enemy = None
        while running:
            screen.fill ((0,0,0))
            if gamephase == 'win':
                screen.blit(bigfont.render('Victory !', False, (255, 255, 255)),(600,300))
            elif gamephase == 'loss':
                screen.blit(bigfont.render('Game Over !', False, (255, 255, 255)),(600,300))
            else:
                screen.blit(wallpaper, (0, 0))
                screen.blit(COIN, (1450, 50))
                screen.blit(bigfont.render(f'{player.coins}', False, (0, 0, 0)), (1350, 50))
                screen.blit(LIVES, (50, 50))
                screen.blit(bigfont.render(f'{player.lives}', False, (0, 0, 0)), (150, 50))
                screen.blit(WINS, (50, 200))
                screen.blit(bigfont.render(f'{player.wins}', False, (0, 0, 0)), (150, 200))
                screen.blit(NEXT, (1450, 450))
                screen.blit(font.render('Space/Enter', False, (255, 255, 255)),(1400,550))
                if gamephase == 'shop':
                    screen.blit(REROLL, (900, 750))
                    screen.blit(font.render('R', False, (255, 255, 255)),(930,850))
                    screen.blit(SELL, (750, 780))
                    screen.blit(FREEZE, (830, 780))
                    screen.blit(font.render('F', False, (255, 255, 255)),(810,850))
                    for i in range(6):
                        if player.shop[i] != None:
                            if player.shop[i].frozen:
                                pygame.draw.rect(screen, (4, 134, 177), pygame.Rect(1600-(100*(i+1)),750, 100, 100))
                    if inp[0] != None:
                        if inp[0] < 5:
                            pygame.draw.rect(screen, ( 230, 201, 32), pygame.Rect(300-(75*inp[0]),600, 100, 100))
                        elif inp[0] < 11:
                            pygame.draw.rect(screen, ( 230, 201, 32), pygame.Rect(1600-(100*(inp[0]-4)),750, 100, 100))
                    for i in range(5):
                        if player.warband[i] != None:
                            temp = player.warband[i]
                            if temp != None:
                                screen.blit(findanimaltoshow(temp.name),(300-(75*i),600))
                                screen.blit(font.render(f'{i+1}', False, (0, 0, 0)),(340 - (75*i),560))
                                screen.blit(smallfont.render(f'ATK {temp.power}', False, (255, 255, 255)),(300 - (75*i),710))
                                screen.blit(smallfont.render(f'DEF {temp.defence}', False, (255, 255, 255)),(300 - (75*i),740))
                                screen.blit(smallfont.render(f'LVL {temp.level}', False, (255, 255, 255)),(300 - (75*i),770))
                                screen.blit(smallfont.render(f'EXP {temp.xp}', False, (255, 255, 255)),(300 - (75*i),800))
                                trait = 'N/A'if temp.trait == None else ''
                                screen.blit(smallfont.render(f'T {trait}', False, (255, 255, 255)),(300 - (75*i),830))
                                if trait == '':
                                    screen.blit(pygame.transform.scale(findfoodtoshow(temp.trait), (40, 40)),(320 - (75*i),830))
                    for i in range(4):
                        if player.shop[i] != None:
                            temp = findanimaltoshow(player.shop[i].name)
                            if temp != None:
                                screen.blit(temp,(1600-(100*(i+1)),750))
                                screen.blit(font.render(findkeytoshow(i), False, (255, 255, 255)),(1630-(100*(i+1)),850))
                    for i in range(4,6):
                        if player.shop[i] != None:
                            temp = findfoodtoshow(player.shop[i].name)
                            if temp != None:
                                screen.blit(temp,(1600-(100*(i+1)),750))
                                screen.blit(font.render(findkeytoshow(i), False, (255, 255, 255)),(1630-(100*(i+1)),850))
                elif gamephase == 'battle' and enemy != None:
                    for i in range(5):
                        if playercopy.warband[i] != None:
                            temp = playercopy.warband[i]
                            if temp != None:
                                screen.blit(findanimaltoshow(temp.name),(300-(75*i),600))
                                screen.blit(font.render(f'{i+1}', False, (0, 0, 0)),(340 - (75*i),560))
                                screen.blit(smallfont.render(f'ATK {temp.power}', False, (255, 255, 255)),(300 - (75*i),710))
                                screen.blit(smallfont.render(f'DEF {temp.defence}', False, (255, 255, 255)),(300 - (75*i),740))
                                screen.blit(smallfont.render(f'LVL {temp.level}', False, (255, 255, 255)),(300 - (75*i),770))
                                screen.blit(smallfont.render(f'EXP {temp.xp}', False, (255, 255, 255)),(300 - (75*i),800))
                                trait = 'N/A'if temp.trait == None else ''
                                screen.blit(smallfont.render(f'T {trait}', False, (255, 255, 255)),(300 - (75*i),830))
                                if trait == '':
                                    screen.blit(pygame.transform.scale(findfoodtoshow(temp.trait), (40, 40)),(320 - (75*i),830))
                    for i in range(5):
                        if enemy.warband[i] != None:
                            temp = enemy.warband[i]
                            if temp != None:
                                screen.blit(findanimaltoshow(temp.name),(1600-(300-(75*i)),600))
                                screen.blit(font.render(f'{i+1}', False, (0, 0, 0)),(1600-(340 - (75*i)),560))
                                screen.blit(smallfont.render(f'ATK {temp.power}', False, (255, 255, 255)),(1600-(300 - (75*i)),710))
                                screen.blit(smallfont.render(f'DEF {temp.defence}', False, (255, 255, 255)),(1600-(300 - (75*i)),740))
                                screen.blit(smallfont.render(f'LVL {temp.level}', False, (255, 255, 255)),(1600-(300 - (75*i)),770))
                                screen.blit(smallfont.render(f'EXP {temp.xp}', False, (255, 255, 255)),(1600-(300 - (75*i)),800))
                                trait = 'N/A'if temp.trait == None else ''
                                screen.blit(smallfont.render(f'T {trait}', False, (255, 255, 255)),(1600-(300 - (75*i)),830))
                                if trait == '':
                                    screen.blit(pygame.transform.scale(findfoodtoshow(temp.trait), (40, 40)),(1600-(320 - (75*i)),830))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if mode != 'arena':
                        sendMessege(DISCONNECT)
                    running = False
            keys = pygame.key.get_pressed()
            if gamephase == 'newday':
                player.coins = 10
                for i in range(4):
                    if player.shop[i] == None:
                        temp = getpet(player.day)
                        player.shop[i] = Pet(name=temp.name,power=temp.power,defence= temp.defence)
                for i in range(4,6):
                    if player.shop[i] == None:
                        temp = getfood(player.day)
                        player.shop[i] = Food(name=temp.name)
                for i in range(5):
                    if player.warband[i] != None:
                        if player.warband[i].name == 'Giraffe':
                            tostatup = []
                            for h in range(i-1,-1,-1):
                                if player.warband[h] != None:
                                    tostatup.append(h)
                                if len(tostatup) >= player.warband[i].level:
                                    break
                            if tostatup != []:
                                for _ in tostatup:
                                    player.warband[_].power += 1
                                    player.warband[_].defence += 1
                gamephase = 'shop'
            elif gamephase == 'shop':
                if inp[1] == None:
                    if keys[pygame.K_1] or keys[pygame.K_KP1]:
                        if not held:
                            if inp[0] == None:
                                inp[0] = 0
                            else:
                                inp[1] = 0
                        held = True
                    elif keys[pygame.K_2] or keys[pygame.K_KP2]:
                        if not held:
                            if inp[0] == None:
                                inp[0] = 1
                            else:
                                inp[1] = 1
                        held = True
                    elif keys[pygame.K_3] or keys[pygame.K_KP3]:
                        if not held:
                            if inp[0] == None:
                                inp[0] = 2
                            else:
                                inp[1] = 2
                        held = True
                    elif keys[pygame.K_4] or keys[pygame.K_KP4]:
                        if not held:
                            if inp[0] == None:
                                inp[0] = 3
                            else:
                                inp[1] = 3
                        held = True
                    elif keys[pygame.K_5] or keys[pygame.K_KP5]:
                        if not held:
                            if inp[0] == None:
                                inp[0] = 4
                            else:
                                inp[1] = 4
                        held = True
                    elif keys[pygame.K_q]:
                        if not held:
                            if inp[0] == None:
                                inp[0] = 5
                        held = True
                    elif keys[pygame.K_w]:
                        if not held:
                            if inp[0] == None:
                                inp[0] = 6
                        held = True
                    elif keys[pygame.K_e]:
                        if not held:
                            if inp[0] == None:
                                inp[0] = 7
                        held = True
                    elif keys[pygame.K_a]:
                        if not held:
                            if inp[0] == None:
                                inp[0] = 8
                        held = True
                    elif keys[pygame.K_s]:
                        if not held:
                            if inp[0] == None:
                                inp[0] = 9
                        held = True
                    elif keys[pygame.K_d]:
                        if not held:
                            if inp[0] == None:
                                inp[0] = 10
                        held = True
                    elif keys[pygame.K_f]:
                        if not held and inp[0] != None:
                            inp[1] = 11
                        held = True
                    elif keys[pygame.K_r]:
                        if not held and player.coins > 0:
                            for i in range(4):
                                temp = getpet(player.day)
                                player.shop[i] = Pet(name=temp.name,power=temp.power,defence= temp.defence)
                            for i in range(4,6):
                                temp = getfood(player.day)
                                player.shop[i] = Food(name = temp.name)
                            player.coins -= 1
                        held = True
                    elif keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER] or keys[pygame.K_SPACE]:
                        gamephase = 'battleprep'
                    else:
                        held = False
                else:
                    if inp[1] == 11:
                        if inp[0] < 5:
                            if player.warband[inp[0]] != None:
                                player.coins += 1 if player.warband[inp[0]].name != 'Pig' else 1 + player.warband[inp[0]].level
                                if player.warband[inp[0]].name == 'Duck':
                                    for h in range(4):
                                        player.shop[h].defence += player.warband[inp[0]].level
                                elif player.warband[inp[0]].name == 'Beaver':
                                    tostatup = []
                                    for h in range(5):
                                        if player.warband[h] != None and h != inp[0]:
                                            tostatup.append(h)
                                    if tostatup != []:
                                        for _ in range(2):
                                            player.warband[random.choice(tostatup)].power += player.warband[inp[0]].level
                                player.warband[inp[0]] = None
                        elif inp[0]<11:
                            player.shop[inp[0]-5].frozen = not player.shop[inp[0]-5].frozen
                    elif inp[0] < 5:
                        if inp[1] < 5:
                            player.warband[inp[0]],player.warband[inp[1]] = player.warband[inp[1]],player.warband[inp[0]]
                    elif inp[0] < 9 and player.coins > 2:
                        if player.shop[inp[0]-5].name == "Cricket" or player.shop[inp[0]-5].name == "Pig" or player.shop[inp[0]-5].name == "Duck" or player.shop[inp[0]-5].name == "Beaver":
                            for _ in range(5):
                                if player.warband[_] != None:
                                    if player.warband[_].name == 'Dragon':
                                        for __ in range(5):
                                            if player.warband[__] != None:
                                                player.warband[__].power += player.warband[_].level
                                                player.warband[__].defence += player.warband[_].level
                        if player.warband[inp[1]] == None:
                            player.warband[inp[1]] = player.shop[inp[0]-5]
                            temp = getpet(player.day)
                            player.shop[inp[0]-5] = Pet(name=temp.name,power=temp.power,defence= temp.defence)
                            player.coins -=3
                        elif player.warband[inp[1]].name == player.shop[inp[0]-5].name:
                            player.warband[inp[1]].addXp()
                            temp = getpet(player.day)
                            player.shop[inp[0]-5] = Pet(name=temp.name,power=temp.power,defence= temp.defence)
                            player.coins -=3
                    elif player.warband[inp[1]] != None:
                        if player.shop[inp[0]-5].name =="Honey" and player.coins > 2:
                            player.warband[inp[1]].trait = 'Honey'
                            temp = getfood(player.day)
                            player.shop[inp[0]-5] = Food(name = temp.name)
                            player.coins -=3
                        elif player.shop[inp[0]-5].name == "Apple" and player.coins > 2:
                            player.warband[inp[1]].power += 1
                            player.warband[inp[1]].defence += 1
                            temp = getfood(player.day)
                            player.shop[inp[0]-5] = Food(name = temp.name)
                            player.coins -=3
                        elif player.shop[inp[0]-5].name == "Sleeping Pill" and player.coins > 0:
                            player.warband = player.warband[inp[1]].die(selfnum = inp[1],warband = player.warband)
                            temp = getfood(player.day)
                            player.shop[inp[0]-5] = Food(name = temp.name)
                            player.coins -=1
                        elif player.shop[inp[0]-5].name == "Meat Bone" and player.coins > 2:
                            player.warband[inp[1]].trait = 'Meat Bone'
                            temp = getfood(player.day)
                            player.shop[inp[0]-5] = Food(name = temp.name)
                            player.coins -=3
                        elif player.shop[inp[0]-5].name == "Garlic" and player.coins > 2:
                            player.warband[inp[1]].trait = 'Garlic'
                            temp = getfood(player.day)
                            player.shop[inp[0]-5] = Food(name = temp.name)
                            player.coins -=3
                        elif player.shop[inp[0]-5].name == "Salad" and player.coins > 2:
                            temp = [x for x in range(len(player.warband)) if player.warband[x] != None]
                            if len(temp) > 0:
                                for i in range(2):
                                    j = random.choice(temp)
                                    player.warband[j].power += 1
                                    player.warband[j].defence += 1
                                temp = getfood(player.day)
                                player.shop[inp[0]-5] = Food(name = temp.name)
                                player.coins -=3
                        elif player.shop[inp[0]-5].name == "Pear" and player.coins > 2:
                            player.warband[inp[1]].power += 2
                            player.warband[inp[1]].defence += 2
                            temp = getfood(player.day)
                            player.shop[inp[0]-5] = Food(name = temp.name)
                            player.coins -=3
                        elif player.shop[inp[0]-5].name == "Chili" and player.coins > 2:
                            player.warband[inp[1]].trait = 'Chili'
                            temp = getfood(player.day)
                            player.shop[inp[0]-5] = Food(name = temp.name)
                            player.coins -=3
                        elif player.shop[inp[0]-5].name == "Chocolate" and player.coins > 2:
                            player.warband[inp[1]].addXp()
                            temp = getfood(player.day)
                            player.shop[inp[0]-5] = Food(name = temp.name)
                            player.coins -=3
                        elif player.shop[inp[0]-5].name == "Sushi" and player.coins > 2:
                            temp = [x for x in range(len(player.warband)) if player.warband[x] != None]
                            if len(temp) > 0:
                                for i in range(3):
                                        j = random.choice(temp)
                                        player.warband[j].power += 1
                                        player.warband[j].defence += 1
                                temp = getfood(player.day)
                                player.shop[inp[0]-5] = Food(name = temp.name)
                                player.coins -=3
                        elif player.shop[inp[0]-5].name == "Steak" and player.coins > 2:
                            player.warband[inp[1]].trait = 'Steak'
                            temp = getfood(player.day)
                            player.shop[inp[0]-5] = Food(name = temp.name)
                            player.coins -=3
                        elif player.shop[inp[0]-5].name == "Melon" and player.coins > 2:
                            player.warband[inp[1]].trait = 'Melon'
                            temp = getfood(player.day)
                            player.shop[inp[0]-5] = Food(name = temp.name)
                            player.coins -=3
                        elif player.shop[inp[0]-5].name == "Pizza" and player.coins > 2:
                            temp = [x for x in range(len(player.warband)) if player.warband[x] != None]
                            if len(temp) > 0:
                                for i in range(2):
                                    j = random.choice(temp)
                                    player.warband[j].power += 2
                                    player.warband[j].defence += 2
                                temp = getfood(player.day)
                                player.shop[inp[0]-5] = Food(name = temp.name)
                                player.coins -=3
                    held = False
                    inp[0] , inp[1] = (None,None)
            elif gamephase == 'battleprep':
                playercopyband = []
                for _ in player.warband:
                    if _ != None:
                        playercopyband.append(Pet(name=_.name, power=_.power ,defence=_.defence ,trait= _.trait,xp = _.xp, level = _.level))
                for _ in range(5 - len(playercopyband)):
                    playercopyband.append(None)
                playercopy = Player(warband = playercopyband,shop = None,day = player.day,coins = player.coins,lives = player.lives,wins = player.wins)
                if mode == 'arena':
                    enemy = random.choice(list(Player.select().where(Player.day == playercopy.day)))
                    enemy.warband = str2obj(enemy.warband)
                else:
                    sendMessege(f'saveplayer¶{obj2str(player)}')
                    sendMessege('getenemy')
                    enemy = str2obj(reciveMessege())
                Player.create(warband = obj2str(player.warband),shop = obj2str(player.shop),day = player.day,coins = player.coins,lives = player.lives,wins = player.wins)
                doiattack = random.choice([True,False])
                gamephase = 'battle'
                for i in range(5):
                    if playercopy.warband[i] != None:
                        if playercopy.warband[i].name == 'Crab':
                            try:
                                mosthealth = max(playercopy.warband[x].defence for x in range(5) if (x != i and playercopy.warband[x] != None))
                                playercopy.warband[i].defence += mosthealth *(playercopy.warband[i].level/2)
                            except:
                                pass
                        elif playercopy.warband[i].name == 'Dodo':
                            for j in range(i-1,-1,-1):
                                if playercopy.warband[j] != None:
                                    playercopy.warband[j].power += playercopy.warband[i].power *(playercopy.warband[i].level/2)
                                    break
                        elif playercopy.warband[i].name == 'Parrot':
                            for j in range(i-1,-1,-1):
                                if playercopy.warband[j] != None:
                                    playercopy.warband[i].name += playercopy.warband[j].name
                                    break
                        elif playercopy.warband[i].name == 'Armadillo':
                            for j in range(5):
                                if playercopy.warband[j] != None:
                                    playercopy.warband[j].defence += 8*playercopy.warband[i].level
                                if enemy.warband[j] != None:
                                    enemy.warband[j].defence += 8*playercopy.warband[i].level
                        elif playercopy.warband[i].name == 'Skunk':
                            max = [-99 , -1]
                            for j in range(5):
                                if enemy.warband[j] != None:
                                    if enemy.warband[j].defence > max[0]:
                                        max = [enemy.warband[j].defence,j]
                    if enemy.warband[i] != None:
                        if enemy.warband[i].name == 'Crab':
                            try:
                                mosthealth = max(enemy.warband[x].defence for x in range(5) if (x != i and playercopy.warband[x] != None))
                                enemy.warband[i].defence += mosthealth *(enemy.warband[i].level/2)
                            except:
                                pass
                        elif enemy.warband[i].name == 'Dodo':
                            for j in range(i-1,-1,-1):
                                if enemy.warband[j] != None:
                                    enemy.warband[j].power += enemy.warband[i].power *(enemy.warband[i].level/2)
                                    break
                        elif enemy.warband[i].name == 'Parrot':
                            for j in range(i-1,-1,-1):
                                if enemy.warband[j] != None:
                                    enemy.warband[i].name += enemy.warband[j].name
                                    break
                        elif enemy.warband[i].name == 'Armadillo':
                            for j in range(5):
                                if playercopy.warband[j] != None:
                                    playercopy.warband[j].defence += 8*playercopy.warband[i].level
                                if enemy.warband[j] != None:
                                    enemy.warband[j].defence += 8*playercopy.warband[i].level
                        elif enemy.warband[i].name == 'Skunk':
                            max = [-99 , -1]
                            for j in range(5):
                                if playercopy.warband[j] != None:
                                    if playercopy.warband[j].defence > max[0]:
                                        max = [playercopy.warband[j].defence,j]
                            playercopy.warband[max[1]].defence -= (playercopy.warband[max[1]].defence * (33*enemy.warband[i].level)) // 100
            elif gamephase == 'battle':
                if doiattack:
                    attacker = None
                    for i in range(5):
                        if playercopy.warband[i] != None:
                            attacker = playercopy.warband[i]
                            break
                    if attacker != None:
                        attacker.attack(i,playercopy.warband,enemy.warband)
                        for i in range(5):
                            if playercopy.warband[i] != None:
                                if playercopy.warband[i].defence <1:
                                    playercopy.warband[i].die(i,playercopy.warband)
                            if enemy.warband[i] != None:
                                if enemy.warband[i].defence <1:
                                    enemy.warband[i].die(i,enemy.warband)
                    doiattack = not doiattack
                else:
                    attacker = None
                    for i in range(5):
                        if enemy.warband[i] != None:
                            attacker = enemy.warband[i]
                            break
                    if attacker != None:
                        attacker.attack(i,enemy.warband,playercopy.warband)
                        for i in range(5):
                            if playercopy.warband[i] != None:
                                if playercopy.warband[i].defence <1:
                                    playercopy.warband[i].die(i,playercopy.warband)
                            if enemy.warband[i] != None:
                                if enemy.warband[i].defence <1:
                                    enemy.warband[i].die(i,enemy.warband)
                    doiattack = not doiattack
                dead = 0
                enemydead = 0
                for i in range(5):
                    if playercopy.warband[i] == None:
                        dead +=1
                    if enemy.warband[i] == None:
                        enemydead +=1
                if enemydead == 5:
                    player.wins += 1
                    gamephase = 'newday'
                    player.day += 1
                elif dead == 5:
                    player.lives -= 1
                    gamephase = 'newday'
                    player.day += 1
                if player.wins >= 10:
                    gamephase = 'win'
                elif player.lives <= 0:
                    gamephase = 'loss'
                time.sleep(1)
            elif gamephase == 'win' or gamephase == 'loss':
                ...    
        pygame.quit()
    def playArena():
        player = Player(warband = [None,None,None,None,None],shop = [None,None,None,None,None,None],day = 1,coins = 0,lives = 4,wins = 0)
        loginWindow.destroy()
        playpygame("arena",player)
    def playVS():
        def newVS():
            sendMessege('newlobby')
            lobbyuuid = reciveMessege()
            uuidinput.delete(0, tk.END)
            uuidinput.insert(0, lobbyuuid)
        def connectVS():
            sendMessege(f'connectlobby¶{uuidinput.get()}')
            signupattempt = reciveMessege()
            if signupattempt == '¶':
                loginWindow.destroy()
                player = Player(warband = [None,None,None,None,None],shop = [None,None,None,None,None,None],day = 1,coins = 10,lives = 4,wins = 0)
                player.ready = False
                playpygame("vs",player)
            else :
                tk.Label(loginWindow,text="Failed").pack()
        client.connect(ADDR)
        arenamodebutton.destroy()
        vsbutton.destroy()
        uuidlabel = tk.Label(loginWindow,text="UUID:")
        uuidlabel.pack()
        uuidinput = tk.Entry(loginWindow)
        uuidinput.pack()
        signupbotton = tk.Button(loginWindow,text="create lobby",command=newVS)
        signupbotton.pack()
        signupbotton = tk.Button(loginWindow,text="Connect to lobby",command=connectVS)
        signupbotton.pack()
    loginWindow = tk.Tk()
    arenamodebutton = tk.Button(loginWindow,text="Play arena mode",command=playArena)
    arenamodebutton.pack()
    vsbutton = tk.Button(loginWindow,text="connect / create VS mode lobby",command=playVS)
    vsbutton.pack()
    loginWindow.mainloop()
if __name__ == '__main__':
    main()