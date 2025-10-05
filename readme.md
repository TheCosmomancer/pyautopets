# Super Auto Pets Clone

A Python-based implementation of a Super Auto Pets-style auto-battler game with local and networked multiplayer modes. Written for Advanved programming final class project.

## Features

- **Arena Mode**: Play against AI opponents with progressively harder teams
- **VS Mode**: Connect with other players over a network for PvP battles
- **Shop System**: Buy pets and food items to strengthen your warband
- **Combat System**: Automated turn-based battles with special pet abilities and trait interactions
- **Persistence**: SQLite database stores game history and arena opponents

## Requirements

- Python 3.x
- pygame
- peewee
- tkinter (usually included with Python)

## Installation

```bash
pip install pygame peewee
```

## Setup

1. Initialize the database with pre-configured opponents:
```bash
python filldb.py
```

2. For VS mode, start the server:
```bash
python server.py
```

## Running

Launch the game client:
```bash
python client.py
```

Choose between Arena mode (single player) or VS mode (multiplayer).

## Gameplay

- Use number keys (1-5) to select warband slots
- Use Q/W/E/A/S/D to select shop items
- Press F to freeze/sell items
- Press R to reroll the shop
- Press Space/Enter to start battle

## Game Elements

- **Pets**: 24 different pets across 6 tiers with unique combat abilities
- **Food**: 13 food items that buff pets or provide special traits
- **Traits**: Honey, Meat Bone, Garlic, Peanut, Chili, Steak, Melon

## Technical Details

- Client-server architecture for multiplayer
- Object serialization using pickle for network transmission
- Pygame-based UI with custom sprite rendering
- Turn-based combat resolution with ability triggers

---

*readme written with AI.*