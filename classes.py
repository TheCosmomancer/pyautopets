import hashlib
import pickle
import base64
import random
from peewee import *
history = SqliteDatabase('history.db')
def passen (password):
    h = hashlib.sha256()
    h.update(password.encode())
    hashed_password = h.hexdigest()
    return hashed_password
class Player(Model):
    warband = CharField()
    shop = CharField()
    day = IntegerField()
    coins = IntegerField()
    lives = IntegerField()
    wins = IntegerField()
    class Meta:
        database = history
class Pet():
    def __init__(self,name,power,defence,trait=None,frozen=False,xp = 0 ,level = 1):
        self.name = name
        self.power = power
        self.defence = defence
        self.trait = trait
        self.frozen = frozen
        self.xp = xp
        self.level = level
    isfood = False
    ispet = True
    def addXp(self):
        self.xp += 1
        if self.level == 1 and self.xp == 2:
            self.level,self.xp = 2,0
        elif self.level == 2 and self.xp == 3:
            self.level,self.xp = 3,0
    def die(self,selfnum,warband):
        place = list()
        if self.name == 'Cricket':
            place.append(Pet(name = 'Cricklet',power = self.level,defence = self.level))
        elif self.name == 'Spider':
            place.append(random.choice([
                Pet(name="Sheep",power=2,defence=2),
                Pet(name="Dodo",power=3,defence=2),
                Pet(name="Ox",power=1,defence=3),
                Pet(name="Camel",power=3,defence=4)]))
        elif self.name == 'Sheep':
            for i in range(2):
                place.append(Pet(name = 'Sheeplet',power = self.level*2,defence = self.level*2))
        elif self.name == 'Flamingo':
            j = 0
            for i in range(selfnum,len(warband)):
                if warband[i] != None:
                    warband[i].power += self.level
                    warband[i].defence += self.level
                    j += 1
                if j >= 2 :
                    break
        elif self.name == 'Turtle':
            j = 0
            for i in range(selfnum,len(warband)):
                if warband[i] != None:
                    warband[i].trait = 'Melon'
                    j += 1
                if j >= self.level :
                    break
        elif self.name == 'Deer':
            place.append(Pet(name = 'Bus',power = self.level*5,defence = self.level*3,trait='Chili'))
        elif self.name == 'Rooster':
            for i in range(self.level):
                place.append(Pet(name = 'Chicken',power = self.power//2,defence = 1))
        elif self.name == 'Mammoth':
            for pet in warband:
                if pet != None:
                    pet.power += self.level*2
                    pet.defence += self.level *2
        elif self.trait == 'Honey':
            place.append(Pet(name = 'Bee',power = 1,defence=1))
        warband[selfnum] = None
        for pet in warband:
            if pet != None:
                if pet.name == 'Shark':
                    pet.power += pet.level*2
                    pet.defence += pet.level*2
        i = 0
        for j in range(len(place)):
            for i in range(len(warband)):
                if warband[i] == None:
                    warband[i] = place[j]
                    place.pop(j)
                    break
            if i == 5:
                break
        return warband
    def attack(self,selfnum,warband,enemyband):
        def evaldamage(attacker,defender):
            estimatedamage = attacker.power
            if attacker.trait == "Meat Bone":
                estimatedamage += 3
            if defender.trait == "Garlic":
                estimatedamage -= 2
            if attacker.trait == "Steak":
                estimatedamage += 20
                attacker.trait = None
            if defender.trait == "Melon":
                estimatedamage -= 20
                defender.trait = None
            if estimatedamage > 0:
                defender.defence -= estimatedamage
            attacker.defence -= defender.power
            return(attacker,defender)
        for target in range(5):
            if enemyband[target] != None:
                break
        if target == 5 and enemyband[target] == None:
            return (warband,None)
        attacks = [self.power]
        for pet in warband:
            if pet != None:
                if pet.name == 'Snake':
                    attacks.append(pet.level*5)
        for i in range(len(attacks)):
            if i == 0:
                if self.name == 'Boar':
                    self.power += 4*self.level
                    self.defence += 2*self.level
                warband[selfnum],enemyband[target] = evaldamage(warband[selfnum],enemyband[target])
                if self.name == 'Peacock':
                    self.power += 3*self.level
                if enemyband[target].name == 'Peacock':
                    enemyband[target].power += 3*enemyband[target].level
                if self.name == 'Camel':
                    for j in range(selfnum+1,5):
                        if warband[j] != None:
                            break
                    if warband[j] != None:
                        warband[j].power += self.level
                        warband[j].defence += 2*self.level
                if enemyband[target].name == 'Camel':
                    for j in range(target+1,5):
                        if enemyband[j] != None:
                            break
                    if enemyband[j] != None:
                        enemyband[j].power += enemyband[target].level
                        enemyband[j].defence += 2*enemyband[target].level
                if self.trait == 'Peanut':
                    enemyband[target].defence = 0
                    self.trait = None
                if enemyband[target].trait == 'Peanut':
                    self.defence = 0
                    enemyband[target].trait = None
                if self.trait == 'Chili':
                    for j in range(target+1,5):
                        if enemyband[j] != None:
                            break
                    if enemyband[j] != None:
                        estimatedamage = 5
                        if enemyband[j].trait == "Garlic":
                            estimatedamage -= 2
                        if enemyband[j].trait == "Melon":
                            estimatedamage -= 20
                            enemyband[j].trait = None
                        if estimatedamage > 0:
                            enemyband[j].defence -= estimatedamage
                        if enemyband[j].name == 'Peacock':
                            enemyband[j].power += 3*enemyband[j].level
                        if enemyband[j].name == 'Camel':
                            for k in range(j+1,5):
                                if enemyband[k] != None:
                                    break
                            if enemyband[k] != None:
                                enemyband[k].power += enemyband[k].level
                                enemyband[k].defence += 2*enemyband[k].level
            else:
                target = random.choice([x for x in range(5) if enemyband[x]!= None])
                estimatedamage = attacks[i]
                if enemyband[target].trait == "Garlic":
                    estimatedamage -= 2
                if enemyband[target].trait == "Melon":
                    estimatedamage -= 20
                    enemyband[target].trait = None
                if estimatedamage > 0:
                    enemyband[target].defence -= estimatedamage
                if enemyband[target].name == 'Peacock':
                    enemyband[target].power += 3*enemyband[target].level
                if enemyband[target].name == 'Camel':
                    for j in range(target+1,5):
                        if enemyband[j] != None:
                            break
                    if enemyband[j] != None:
                        enemyband[j].power += self.level
                        enemyband[j].defence += 2*self.level

class Food():
    def __init__(self,name,frozen=False):
        self.name = name
        self.frozen = frozen
    isfood = True
    ispet = False

PETS = [
#T1 pets
Pet(name="Cricket",power=1,defence=3),#done
Pet(name="Pig",power=4,defence=1),#done
Pet(name="Duck",power=2,defence=3),#done
Pet(name="Beaver",power=3,defence=2),#done
#T2 pets
Pet(name="Crab",power=4,defence=1),#done
Pet(name="Peacock",power=2,defence=5),#done
Pet(name="Flamingo",power=3,defence=2),#done
Pet(name="Spider",power=2,defence=2),#done
#T3 pets
Pet(name="Sheep",power=2,defence=2),#done
Pet(name="Dodo",power=3,defence=2),#done
Pet(name="Giraffe",power=1,defence=2),#done
Pet(name="Camel",power=3,defence=4),#done
#T4 pets
Pet(name="Turtle",power=2,defence=5),#done
Pet(name="Deer",power=4,defence=2),#done
Pet(name="Parrot",power=4,defence=2),#done
Pet(name="Skunk",power=3,defence=5),#done
#T5 pets
Pet(name="Armadillo",power=2,defence=10),#done
Pet(name="Rooster",power=6,defence=4),#done
Pet(name="Shark",power=2,defence=2),#done
Pet(name="Scorpion",power=1,defence=1,trait='Peanut'),#done
#T6 pets
Pet(name="Mammoth",power=4,defence=12),#done
Pet(name="Dragon",power=3,defence=8),#done
Pet(name="Boar",power=10,defence=6),#done
Pet(name="Snake",power=8,defence=3)#done
]
def getpet(day):
    tier = 1 + (day-1)//2
    if tier > 6:
        tier = 6
    choices = []
    for i in range(tier*4):
        choices.append(PETS[i])
    return random.choice(choices)
#T1 foods
FOODS = [
Food(name="Honey"),
Food(name="Apple"),
#T2 foods
Food(name="Sleeping Pill"),
Food(name="Meat Bone"),#done
#T3 foods
Food(name="Garlic"),#done
Food(name="Salad"),
#T4 foods
Food(name="Pear"),
Food(name="Chili"),#TODO
#T5 foods
Food(name="Chocolate"),
Food(name="Sushi"),
#T6 foods
Food(name="Steak"),#done
Food(name="Melon"),#done
Food(name="Pizza")
]
def getfood(day):
    num  = (1 + (day-1)//2)*2
    if num > 10:
        num = 13
    choices = []
    for i in range(num):
        choices.append(FOODS[i])
    return random.choice(choices)
def obj2str(obj):
    return base64.b64encode(pickle.dumps(obj)).decode('utf-8')

def str2obj(pickled_str):
    return pickle.loads(base64.b64decode(pickled_str.encode('utf-8')))