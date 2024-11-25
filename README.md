# Conway's Game of Life - Interactive Python Implementation
## Description
This is an interactive console-based implementation of Conway's Game of Life, a cellular automaton where cells on a grid evolve over time based on simple rules. The program includes advanced features such as saving and loading game states, detecting cycles in the game, and offering both manual and automatic play modes.

## Features
- Interactive Grid Dimensions: Specify the size of the grid at the start of the game.
- Save and Load Game: Resume a previous session or start a new game.
- Cycle Detection: Detects and displays when the game enters a repeating pattern.
- Manual or Automatic Mode:
    - Step through generations manually.
    - Watch the game evolve automatically.
- Cross-Platform Support: Works on both Windows and Unix-like systems.
- Visual Display: Uses symbols (⬜ for live cells and ⬛ for dead cells) to display the grid.

## Getting Started
### Prerequisites
- Python 3.7 or later
- A terminal or command prompt to run the program

### Installation
1. Clone or download the repository to your local machine.
2. Navigate to the folder containing the program files.

## How to Run
1. Ensure all files (main.py, game.py, generator_table.py, etc.) are in the same directory.
2. Run the program by executing the following command in your terminal:
    ```bash
    python main.py
    py main.py
    python3 main.py 
    ```

## How to Play
1. Start the Game:
    - When prompted, enter the size of the grid (e.g., 5 for a 5x5 grid).
    - Choose to resume a previous game (0) or start a new game (1).
2. Game Controls:
    - The grid will display live cells (⬜) and dead cells (⬛).
    - Choose an action:
        - [q]: Quit the game.
        - [a]: Switch to automatic mode.
        - [c]: Step to the next generation manually.
        - Press [Enter] in automatic mode to return to manual control.
3. Cycle Detection:
    -  If a repeating pattern is detected, the program will notify you of the cycle start year.

## File Structure
- main.py: Entry point for the game.
- game.py: Core game logic, including initialization, game state management, and user interactions.
- generator_table.py: Generates the game grid and places live cells based on user input or saved data.
- update_table.py: Handles updating the game grid for each generation.
- print_table.py: Displays the game grid in the console.
- historic.py: Manages the history of game states for cycle detection.
- detection_cycle.py: Implements logic to detect repeating patterns.
- save_game.py: Provides functionality for saving and loading game states to/from a file (save.txt).
- key_controle.py: Handles user input and terminal clearing for both Windows and Unix systems.

## Rules of the Game
1. Any live cell with 2 or 3 neighbors survives.
2. Any dead cell with exactly 3 live neighbors becomes alive.
3. All other live cells die in the next generation, and all other dead cells stay dead.

## Example Gameplay
Initial Grid:
```
⬛⬛⬛⬛⬛
⬛⬜⬜⬜⬛
⬛⬜⬛⬜⬛
⬛⬜⬜⬜⬛
⬛⬛⬛⬛⬛
```
After One Generation:
```
⬛⬛⬛⬛⬛
⬛⬜⬛⬜⬛
⬛⬜⬜⬜⬛
⬛⬜⬛⬜⬛
⬛⬛⬛⬛⬛
```

## Saving and Loading
- Game progress is automatically saved to save.txt.
- The grid, history, and other game states can be restored by selecting 0 when prompted at the start.
- The save is stored in the save.txt file in the following manner: 
    - The save is a list of tables that contains tuples of the positions of each live cell (rows,columns), with the last tuple representing the size of the grid saved when a new game is created (number of rows, number of columns).
    - exemple: 
        ```
            [[[1,1],[3,3]]] <- what we see
            [[[row position of the alive cell,column position of the alive cell],[number of rows,number of column]]]<- what it is
        ```
## Dependencies
No external dependencies are required.

Enjoy playing Conway's Game of Life!