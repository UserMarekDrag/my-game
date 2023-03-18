# PyGame Skill Game
The game was created as a part of a personal project aimed at developing programming skills and pursuing personal interests.

# Gameplay
Feel free to watch the gameplay on the YouTube platform ([link](https://youtu.be/YEv3XwBhZwc/)).

# Storyline
As a beginner adventurer, you set out on your first mission. The first location should be easy and predictable... but it won't be. You will have to fight for survival and until you defeat the wizard, you will not experience peace in this world... Are you ready for this adventure? 

# Running the Game

## Required Software
To run the game, you need to install the Python interpreter version 3.10 or higher on your system ([link](https://www.python.org/downloads/)).  Additionally, you need to install the Pygame library using the pip package manager or use the requirements.txt file.

```bash
pip install -r requirements.txt
```
([link to details](https://www.pygame.org/wiki/GettingStarted]))

## Launching
To start the game, simply run it using the Python interpreter.

```bash
python main.py
```
If you are not in the project folder, you need to provide an absolute path to the file instead of "main.py".


# Program Description
All characters, including monsters and the player, inherit from the Creature class. Each type of monster has its unique way of moving and interacting with the player.
When a monster collides with the player, it triggers a reaction that results in a loss of health points for both the player and the monster. Monsters do not collide with each other.
The game has a Stage system, which means there are five rounds. The game starts with round 1, and with each round, the number and types of monsters increase.
The player's health level is displayed in the upper-left corner. In round 5, the boss's health level is displayed.
The default game settings are located in the config.py file.
The shooting functionality works based on objects in a list with a set limit. These objects are removed after a collision with an enemy or crossing the game boundary. Separate lists are called for the left and right directions. 

# Future Plans
1. Refactoring the entire code to comply with the SOLID principles.
2. Balancing the game to introduce automatically generated levels.

# Author
Marek Drąg
