import hashlib
from peewee import *
db = SqliteDatabase('database.db')
def passen (password):
    h = hashlib.sha256()
    h.update(password.encode())
    hashed_password = h.hexdigest()
    return hashed_password
class Warband(Model):
    #5 , 4 , 3 , 2 , 1 | 1 , 2 , 3 , 4 , 5
    pet1type = CharField()
    pet1stats = CharField()
    pet1mod = CharField()
    pet1xp = IntegerField()
    pet2type = CharField()
    pet2stats = CharField()
    pet2mod = CharField()
    pet2xp = IntegerField()
    pet3type = CharField()
    pet3stats = CharField()
    pet3mod = CharField()
    pet3xp = IntegerField()
    pet4type = CharField()
    pet4stats = CharField()
    pet4mod = CharField()
    pet4xp = IntegerField()
    pet5type = CharField()
    pet5stats = CharField()
    pet5mod = CharField()
    pet5xp = IntegerField()
    class Meta:
        database = db
class Shop(Model):
    pet1 = CharField()
    pet2 = CharField()
    pet3 = CharField()
    pet4 = CharField()
    food1 = CharField()
    food2 = CharField()
    class Meta:
        database = db
class Player(Model):
    username = CharField(unique=True)
    password = CharField()
    warband = ForeignKeyField(Warband, backref='player')
    shop = ForeignKeyField(Shop, backref='player')
    day = IntegerField()
    coins = IntegerField()
    lives = IntegerField()
    class Meta:
        database = db