import hashlib
import pickle
import base64
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

class Food():
    def __init__(self,name,frozen=False):
        self.name = name
        self.frozen = frozen
    isfood = True
    ispet = False
def obj2str(obj):
    return base64.b64encode(pickle.dumps(obj)).decode('utf-8')

def str2obj(pickled_str):
    return pickle.loads(base64.b64decode(pickled_str.encode('utf-8')))
if __name__ == '__main__':
    history.connect()
    history.create_tables([Player])
    #T1 pets
    Cricket = Pet(name="Cricket",power=1,defence=3)
    Pig = Pet(name="Pig",power=4,defence=1)
    Duck = Pet(name="Duck",power=2,defence=3)
    Beaver = Pet(name="Beaver",power=3,defence=2)
    #T2 pets
    Crab = Pet(name="Crab",power=4,defence=1)
    Peacock = Pet(name="Peacock",power=2,defence=5)
    Flamingo = Pet(name="Flamingo",power=3,defence=2)
    Spider = Pet(name="Spider",power=2,defence=2)
    #T3 pets
    Sheep = Pet(name="Sheep",power=2,defence=2)
    Dodo = Pet(name="Dodo",power=3,defence=2)
    Ox = Pet(name="Ox",power=1,defence=3)
    Camel = Pet(name="Camel",power=3,defence=4)
    #T4 pets
    Turtle = Pet(name="Turtle",power=2,defence=5)
    Deer = Pet(name="Deer",power=4,defence=2)
    Parrot = Pet(name="Parrot",power=4,defence=2)
    Skunk = Pet(name="Skunk",power=3,defence=5)
    #T5 pets
    Armadillo = Pet(name="Armadillo",power=2,defence=10)
    Rooster = Pet(name="Rooster",power=6,defence=4)
    Shark = Pet(name="Shark",power=2,defence=2)
    Scorpion = Pet(name="Scorpion",power=1,defence=1)
    #T6 pets
    Mammoth = Pet(name="Mammoth",power=4,defence=12)
    Dragon = Pet(name="Dragon",power=3,defence=8)
    Boar = Pet(name="Boar",power=10,defence=6)
    Snake = Pet(name="Snake",power=8,defence=3)
    #T1 foods
    Honey = Food(name="Honey")
    Apple = Food(name="Apple")
    #T2 foods
    SleepingPill = Food(name="Sleeping Pill")
    MeatBone = Food(name="Meat Bone")
    #T3 foods
    Garlic = Food(name="Garlic")
    Salad = Food(name="Salad")
    #T4 foods
    Pear = Food(name="Pear")
    Chili = Food(name="Chili")
    #T5 foods
    Chocolate = Food(name="Chocolate")
    Sushi = Food(name="Sushi")
    #T6 foods
    Steak = Food(name="Steak")
    Melon = Food(name="Melon")
    Pizza = Food(name="Pizza")