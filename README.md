# Cosmic Invasion

Cosmic Invasion is a classic "Space Invaders" game created using Pygame. The objective of the game is to protect the planet from an alien spaceship invasion. The game offers increasing difficulty, with each level increasing the speed of the enemies.

![screenshot_image](images/screenshot.png)

## Table of Contents

- [Installation](#installation)
- [Running the Game](#running-the-game)
- [Game Rules](#game-rules)
- [Files](#files)
- [Contribution](#contribution)
- [License](#license)

## Installation

To run the game, clone this repository to your local disk:

sh

`git clone https://github.com/your-username/repository-name.git cd repository-name`

You need Python and the Pygame library installed. You can install them using the following commands:

sh

`pip install pygame`

You can also use the requirements.txt file:

sh

`pip install -r requirements.txt`

## Running the Game

To run the game, simply execute the following command in the terminal while in the project directory:

sh

`python space_invaders.py`

## Game Rules

- Use the arrow keys to move your ship left and right.
- Press the spacebar to shoot a bullet.
- Destroy all alien ships to progress to the next level.
- Each subsequent level increases the speed of the enemies.
- The game ends when all your ships are destroyed or when the aliens reach the bottom edge of the screen.

## Files

### Main Game Files

- **space_invaders.py**: Main file that runs the game.
- **settings.py**: Configuration file with game settings.
- **game_functions.py**: File containing the main game functions.
- **game_stats.py**: File managing game statistics.
- **scoreboard.py**: File responsible for displaying scores.
- **button.py**: File defining buttons in the game.
- **ship.py**: File managing the player’s ship.
- **bullet.py**: File managing bullets.
- **invader.py**: File managing alien ships.

### Dependencies

- **pygame**: Library for creating 2D games.

## Contribution

If you want to contribute to the development of this project, open an issue or create a pull request. New features, bug fixes, and code optimizations are always welcome.

## License

The project is available under the MIT license. Details can be found in the LICENSE file.