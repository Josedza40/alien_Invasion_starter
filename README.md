# Alien Invasion - Battle Mode

## Project Description

This project is based on the Alien Invasion game developed during our Python class tutorials. For this project, I selected Track 1: Custom Game Mechanics.

My goal is to add new shooting mechanics to the existing game and improve the gameplay throughout the three milestones.

## Milestone 1 - Core Mechanics

For the first milestone, I implemented two custom shooting features:

**Spread Shot**
- Press S to fire three bullets simultaneously.
- The bullets travel left, straight, and right.
- This mechanic uses horizontal and vertical movement to create different shooting directions.

**Rapid Fire**
- Hold R to fire bullets continuously.
- The game uses `pygame.time.get_ticks()` to control the time between shots.
- Rapid Fire follows the existing bullet limit.

I also temporarily disabled the alien fleet, scoring system, HUD, and Play button to focus on testing the new mechanics.

## Controls

| Key | Action |
|---|---|
| Left Arrow | Move left |
| Right Arrow | Move right |
| Space | Fire a normal bullet |
| S | Fire Spread Shot |
| R (Hold) | Activate Rapid Fire |
| Q | Quit the game |

## How to Run

1. Clone or download the repository.
2. Open the project folder in VS Code or a terminal.
3. Install the required dependencies:

   `python -m pip install -r requirements.txt`

4. Run the game:

   `python alien_invasion.py`

## Milestone Demonstrations

**Milestone_1_Demo:** YouTube link will be added after recording.

**Milestone_2_Demo:** Coming soon.

**Final_Project_Demo:** Coming soon.