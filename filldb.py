from classes import *
if __name__ == '__main__':
    history.connect()
    history.create_tables([Player])
    Player.create(
        warband = obj2str([
        Pet(name="Pig",power=4,defence=1),
        Pet(name="Cricket",power=2,defence=4),
        None,
        None,
        None
        ]),
        shop = ' ',
        day = 1,
        coins = 0,
        lives = 4,
        wins = 0
    )
    Player.create(
        warband = obj2str([
        Pet(name="Pig",power=4,defence=1),
        Pet(name="Cricket",power=3,defence=5),
        Pet(name="Pig",power=4,defence=1),
        Pet(name="Beaver",power=3,defence=2),
        None
        ]),
        shop = ' ',
        day = 2,
        coins = 0,
        lives = 4,
        wins = 0
    )
    Player.create(
        warband = obj2str([
        Pet(name="Cricket",power=4,defence=6,trait='Meat Bone'),
        Pet(name="Crab",power=4,defence=1),
        Pet(name="Spider",power=2,defence=2),
        Pet(name="Beaver",power=3,defence=2),
        None
        ]),
        shop = ' ',
        day = 3,
        coins = 0,
        lives = 4,
        wins = 0
    )
    Player.create(
        warband = obj2str([
        Pet(name="Cricket",power=4,defence=6,trait='Meat Bone'),
        Pet(name="Crab",power=4,defence=1),
        Pet(name="Spider",power=2,defence=2,trait='Honey'),
        Pet(name="Beaver",power=3,defence=2),
        Pet(name="Peacock",power=3,defence=6)
        ]),
        shop = ' ',
        day = 4,
        coins = 0,
        lives = 4,
        wins = 0
    )
    Player.create(
        warband = obj2str([
        Pet(name="Sheep",power=3,defence=3),
        Pet(name="Crab",power=5,defence=2),
        Pet(name="Spider",power=3,defence=3,trait='Honey'),
        Pet(name="Dodo",power=4,defence=3),
        Pet(name="Peacock",power=4,defence=7)
        ]),
        shop = ' ',
        day = 5,
        coins = 0,
        lives = 4,
        wins = 0
    )
    Player.create(
        warband = obj2str([
        Pet(name="Sheep",power=4,defence=4),
        Pet(name="Giraffe",power=2,defence=3),
        Pet(name="Camel",power=4,defence=5),
        Pet(name="Dodo",power=5,defence=4),
        Pet(name="Flamingo",power=4,defence=3,trait='Garlic')
        ]),
        shop = ' ',
        day = 6,
        coins = 0,
        lives = 4,
        wins = 0
    )
    Player.create(
        warband = obj2str([
        Pet(name="Turtle",power=3,defence=6),
        Pet(name="Deer",power=5,defence=3),
        Pet(name="Camel",power=5,defence=6),
        Pet(name="Sheep",power=5,defence=5),
        Pet(name="Giraffe",power=3,defence=4)
        ]),
        shop = ' ',
        day = 7,
        coins = 0,
        lives = 4,
        wins = 0
    )
    Player.create(
        warband = obj2str([
        Pet(name="Turtle",power=4,defence=7),
        Pet(name="Deer",power=6,defence=4),
        Pet(name="Parrot",power=5,defence=3),
        Pet(name="Skunk",power=4,defence=6),
        Pet(name="Camel",power=6,defence=7)
        ]),
        shop = ' ',
        day = 8,
        coins = 0,
        lives = 4,
        wins = 0
    )
    Player.create(
        warband = obj2str([
        Pet(name="Armadillo",power=3,defence=11),
        Pet(name="Rooster",power=7,defence=5),
        Pet(name="Shark",power=3,defence=3),
        Pet(name="Skunk",power=5,defence=7),
        Pet(name="Deer",power=7,defence=5)
        ]),
        shop = ' ',
        day = 9,
        coins = 0,
        lives = 4,
        wins = 0
    )
    Player.create(
        warband = obj2str([
        Pet(name="Armadillo",power=4,defence=12),
        Pet(name="Rooster",power=8,defence=6),
        Pet(name="Scorpion",power=2,defence=2,trait='Peanut'),
        Pet(name="Shark",power=4,defence=4),
        Pet(name="Turtle",power=5,defence=8)
        ]),
        shop = ' ',
        day = 10,
        coins = 0,
        lives = 4,
        wins = 0
    )
    Player.create(
        warband = obj2str([
        Pet(name="Mammoth",power=5,defence=13),
        Pet(name="Dragon",power=4,defence=9),
        Pet(name="Rooster",power=9,defence=7),
        Pet(name="Armadillo",power=5,defence=13),
        Pet(name="Shark",power=5,defence=5)
        ]),
        shop = ' ',
        day = 11,
        coins = 0,
        lives = 4,
        wins = 0
    )
    Player.create(
        warband = obj2str([
        Pet(name="Mammoth",power=6,defence=14),
        Pet(name="Boar",power=11,defence=7),
        Pet(name="Dragon",power=5,defence=10),
        Pet(name="Snake",power=9,defence=4),
        Pet(name="Rooster",power=10,defence=8)
        ]),
        shop = ' ',
        day = 12,
        coins = 0,
        lives = 4,
        wins = 0
    )
    Player.create(
        warband = obj2str([
        Pet(name="Boar",power=12,defence=8),
        Pet(name="Mammoth",power=7,defence=15),
        Pet(name="Snake",power=10,defence=5),
        Pet(name="Dragon",power=6,defence=11),
        Pet(name="Scorpion",power=3,defence=3,trait='Peanut')
        ]),
        shop = ' ',
        day = 13,
        coins = 0,
        lives = 4,
        wins = 0
    )