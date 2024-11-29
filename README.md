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
⬛⬛⬛⬛⬛
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


# Jeu de la Vie de Conway - Implémentation Interactive en Python
## Description
Il s'agit d'une implémentation interactive du Jeu de la Vie de Conway, un automate cellulaire où les cellules sur une grille évoluent au fil du temps selon des règles simples. Le programme comprend des fonctionnalités avancées telles que l'enregistrement et le chargement des états du jeu, la détection de cycles dans le jeu et propose des modes de jeu manuels et automatiques.

## Fonctionnalités
- Dimensions de la grille interactives : Spécifiez la taille de la grille au début du jeu.
- Enregistrer et charger le jeu : Reprenez une session précédente ou commencez une nouvelle partie.
- Détection de cycles : Détecte et affiche lorsque le jeu entre dans un motif récurrent.
- Mode manuel ou automatique :
- Passez manuellement d'une génération à l'autre.
- Regardez le jeu évoluer automatiquement.
- Support multiplateforme : Fonctionne à la fois sur Windows et les systèmes Unix.
- Affichage visuel : Utilise des symboles (⬜ pour les cellules vivantes et ⬛ pour les cellules mortes) pour afficher la grille.

## Prise en main
### Prérequis
- Python 3.7 ou version ultérieure
- Un terminal ou une ligne de commande pour exécuter le programme
### Installation
- Clonez ou téléchargez le repository sur votre machine locale.
- Naviguez vers le dossier contenant les fichiers du programme.

## Comment lancer le jeu
1. Assurez-vous que tous les fichiers (main.py, game.py, generator_table.py, etc.) sont dans le même répertoire.
2. Exécutez le programme en lançant la commande suivante dans votre terminal :
    ```
    python main.py
    py main.py
    python3 main.py 
    ```

## Comment jouer
1. Démarrer le jeu :
    - Lorsque vous y êtes invité, entrez la taille de la grille (par exemple, 5 pour une grille de 5x5).
    - Choisissez de reprendre une partie précédente (0) ou de commencer une nouvelle partie (1).
2. Commandes du jeu :
    - La grille affichera les cellules vivantes (⬜) et mortes (⬛).
    - Choisissez une action :
        - [q] : Quitter le jeu.
        - [a] : Passer en mode automatique.
        - [c] : Passer à la génération suivante manuellement.
        - Appuyez sur [Entrée] en mode automatique pour revenir au mode manuel.
    - Détection des cycles :
        - Si un motif récurrent est détecté, le programme vous informera de l'année du début du cycle.

## Structure des fichiers
- main.py : Point d'entrée du jeu.
- game.py : Logique principale du jeu, y compris l'initialisation, la gestion de l'état du jeu et les interactions avec l'utilisateur.
- generator_table.py : Génère la grille du jeu et place les cellules vivantes en fonction des entrées de l'utilisateur ou des données enregistrées.
- update_table.py : Gère la mise à jour de la grille du jeu pour chaque génération.
- print_table.py : Affiche la grille du jeu dans le terminal.
- historic.py : Gère l'historique des états du jeu pour la détection des cycles.
- detection_cycle.py : Implémente la logique de détection des motifs récurrents.
- save_game.py : Fournit des fonctionnalités pour enregistrer et charger les états du jeu depuis/vers un fichier (save.txt).
- key_controle.py : Gère les entrées utilisateur et le nettoyage du terminal pour les systèmes Windows et Unix.

## Règles du jeu
- Toute cellule vivante avec 2 ou 3 voisins survit.
- Toute cellule morte avec exactement 3 voisins vivants devient vivante.
- Toutes les autres cellules vivantes meurent à la génération suivante, et toutes les autres cellules mortes restent mortes.

## Exemple de jeu
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
⬛⬛⬛⬛⬛
⬛⬜⬛⬜⬛
⬛⬛⬛⬛⬛
```

## Enregistrement et Chargement
- La progression du jeu est automatiquement enregistrée dans le fichier save.txt.
- La grille, l'historique et d'autres états du jeu peuvent être restaurés en sélectionnant 0 lors du démarrage du jeu.
- La sauvegarde est stockée dans le fichier save.txt de la manière suivante :
    - La sauvegarde est une liste de tables contenant des tuples représentant les positions des cellules vivantes (lignes, colonnes), le dernier tuple représentant la taille de la grille sauvegardée lorsqu'un nouveau jeu est créé (nombre de lignes, nombre de colonnes).
    - Exemple :
        ```
        [[[1,1],[3,3]]] <- ce que nous voyons
        [[[position de la cellule vivante, position de la cellule vivante],[nombre de lignes, nombre de colonnes]]] <- ce que c'est
        ```

## Dépendances
Aucune dépendance externe n'est requise.

Amusez-vous bien avec le Jeu de la Vie de Conway !