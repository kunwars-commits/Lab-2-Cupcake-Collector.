# Lab 2: Cupcake Collector
A 2D platformer game built using Pygame and Python's `asyncio` library, compiled for web browsers using Pygbag.
## Live Game Link
Play directly in your browser.
## Game Description
In **Cupcake Collector**, you control a cute red character navigating across floating platforms. Your goal is to collect all 10 delicious cupcakes scattered across the stage while using physics, gravity, and timing to jump between platforms.
## How to Play
- **Left Arrow**: Move Left
- **Right Arrow**: Move Right
- **Up Arrow / Spacebar**: Jump
- **R Key**: Restart game after collecting all cupcakes
## Objective
Collect all 10 cupcakes to win! A counter at the top-left tracks how many cupcakes remain. Sound effects play when you jump, collect a cupcake, and complete the game.
## Project Structure
- `main.py` - Core game loop, player physics, platform collision detection, and cupcake collection logic
- `assets/player.png` - Player character sprite
- `assets/cupcake.png` - Cupcake collectible sprite
- `assets/jump.ogg` - Jump sound effect
- `assets/collect.ogg` - Cupcake collection sound effect
- `assets/win.ogg` - Victory fanfare
- `README.md` - Game overview and instructions
## Running Locally
1. Install Python 3.10+ and Pygame:
   ```bash
   pip install pygame
   ```
2. Run the game:
   ```bash
   python main.py
   ```
