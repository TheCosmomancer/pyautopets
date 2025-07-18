import hashlib
import pickle
import base64
from peewee import *
def passen (password):
    h = hashlib.sha256()
    h.update(password.encode())
    hashed_password = h.hexdigest()
    return hashed_password
class Player(Model):
    username = CharField(unique=True)
    password = CharField()
    warband = CharField()
    shop = CharField()
    day = IntegerField()
    coins = IntegerField()
    lives = IntegerField()
    class Meta:
        database = db
class Pet():
    def __init__(self,name,power,defence,trait=None,frozen=False):
        self.name = name
        self.power = power
        self.defence = defence
        self.trait = trait
        self.frozen = frozen
    @staticmethod
    def isfood():
        return False
    @staticmethod
    def ispet():
        return True
class Food():
    def __init__(self,name,frozen):
        self.name = name
        self.frozen = frozen
    @staticmethod
    def isfood():
        return True
    @staticmethod
    def ispet():
        return False
def obj2str(obj):
    return base64.b64encode(pickle.dumps(obj)).decode('utf-8')

def str2obj(pickled_str):
    return pickle.loads(base64.b64decode(pickled_str.encode('utf-8')))
if __name__ == '__main__':
    history = SqliteDatabase('history.db')
    history.connect()
    history.create_tables([Player])
    #T1 pets
    PetBank.create(name="Cricket",power=1,defence=3)
    PetBank.create(name="Pig",power=4,defence=1)
    PetBank.create(name="Duck",power=2,defence=3)
    PetBank.create(name="Beaver",power=3,defence=2)
    #T2 pets
    PetBank.create(name="Crab",power=4,defence=1)
    PetBank.create(name="Peacock",power=2,defence=5)
    PetBank.create(name="Flamingo",power=3,defence=2)
    PetBank.create(name="Spider",power=2,defence=2)
    #T3 pets
    PetBank.create(name="Sheep",power=2,defence=2)
    PetBank.create(name="Dodo",power=3,defence=2)
    PetBank.create(name="Ox",power=1,defence=3)
    PetBank.create(name="Camel",power=3,defence=4)
    #T4 pets
    PetBank.create(name="Turtle",power=2,defence=5)
    PetBank.create(name="Deer",power=4,defence=2)
    PetBank.create(name="Parrot",power=4,defence=2)
    PetBank.create(name="Skunk",power=3,defence=5)
    #T5 pets
    PetBank.create(name="Armadillo",power=2,defence=10)
    PetBank.create(name="Rooster",power=6,defence=4)
    PetBank.create(name="Shark",power=2,defence=2)
    PetBank.create(name="Scorpion",power=1,defence=1)
    #T6 pets
    PetBank.create(name="Mammoth",power=4,defence=12)
    PetBank.create(name="Dragon",power=3,defence=8)
    PetBank.create(name="Boar",power=10,defence=6)
    PetBank.create(name="Snake",power=8,defence=3)
    #T1 foods
    FoodBank.create(name="Honey")
    FoodBank.create(name="Apple")
    #T2 foods
    FoodBank.create(name="Sleeping Pill")
    FoodBank.create(name="Meat Bone")
    #T3 foods
    FoodBank.create(name="Garlic")
    FoodBank.create(name="Salad")
    #T4 foods
    FoodBank.create(name="Pear")
    FoodBank.create(name="Chili")
    #T5 foods
    FoodBank.create(name="Chocolate")
    FoodBank.create(name="Sushi")
    #T6 foods
    FoodBank.create(name="Steak")
    FoodBank.create(name="Melon")
    FoodBank.create(name="Pizza")