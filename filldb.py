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
    # Player.create(
    #     warband = obj2str([
            # None,
            # None,
            # None,
            # None,
            # None
    #     ]),
    #     shop = ' ',
    #     day = 5,
    #     coins = 0,
    #     lives = 4,
    #     wins = 0
    # )
    # Player.create(
    #     warband = obj2str([
            # None,
            # None,
            # None,
            # None,
            # None
    #     ]),
    #     shop = ' ',
    #     day = 6,
    #     coins = 0,
    #     lives = 4,
    #     wins = 0
    # )
    # Player.create(
    #     warband = obj2str([
            # None,
            # None,
            # None,
            # None,
            # None
    #     ]),
    #     shop = ' ',
    #     day = 7,
    #     coins = 0,
    #     lives = 4,
    #     wins = 0
    # )
    # Player.create(
    #     warband = obj2str([
            # None,
            # None,
            # None,
            # None,
            # None
    #     ]),
    #     shop = ' ',
    #     day = 8,
    #     coins = 0,
    #     lives = 4,
    #     wins = 0
    # )
    # Player.create(
    #     warband = obj2str([
            # None,
            # None,
            # None,
            # None,
            # None
    #     ]),
    #     shop = ' ',
    #     day = 9,
    #     coins = 0,
    #     lives = 4,
    #     wins = 0
    # )
    # Player.create(
    #     warband = obj2str([
            # None,
            # None,
            # None,
            # None,
            # None
    #     ]),
    #     shop = ' ',
    #     day = 10,
    #     coins = 0,
    #     lives = 4,
    #     wins = 0
    # )
    # Player.create(
    #     warband = obj2str([
            # None,
            # None,
            # None,
            # None,
            # None
    #     ]),
    #     shop = ' ',
    #     day = 11,
    #     coins = 0,
    #     lives = 4,
    #     wins = 0
    # )
    # Player.create(
    #     warband = obj2str([
            # None,
            # None,
            # None,
            # None,
            # None
    #     ]),
    #     shop = ' ',
    #     day = 12,
    #     coins = 0,
    #     lives = 4,
    #     wins = 0
    # )
    # Player.create(
    #     warband = obj2str([
            # None,
            # None,
            # None,
            # None,
            # None
    #     ]),
    #     shop = ' ',
    #     day = 13,
    #     coins = 0,
    #     lives = 4,
    #     wins = 0
    # )