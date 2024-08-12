# Tic-Tac-Toe Game

This is a simple command-line Tic-Tac-Toe game built using Python. The game allows two players to compete against each other by taking turns to place their symbols (X or O) on a 3x3 grid. The goal is to be the first player to get three of their symbols in a row, column, or diagonal.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How to Play](#how-to-play)
- [Game Flow](#game-flow)
- [License](#license)

## Features

- Two-player mode: Player 1 vs. Player 2
- Clean and intuitive command-line interface
- Automatic detection of winning and draw conditions
- Option to replay the game after it ends
- Handles invalid inputs gracefully

## Installation

To run this game on your local machine, you need to have Python installed. Follow these steps to set up the game:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/tic-tac-toe.git
Sure! Here’s the entire response in Markdown format:

\# Tic-Tac-Toe Game

This is a simple command-line Tic-Tac-Toe game built using Python. The game allows two players to compete against each other by taking turns to place their symbols (X or O) on a 3x3 grid. The goal is to be the first player to get three of their symbols in a row, column, or diagonal.

\## Table of Contents

\- [Features](\#features)  
\- [Installation](\#installation)  
\- [Usage](\#usage)  
\- [How to Play](\#how-to-play)  
\- [Game Flow](\#game-flow)  
\- [License](\#license)

\## Features

\- Two-player mode: Player 1 vs. Player 2  
\- Clean and intuitive command-line interface  
\- Automatic detection of winning and draw conditions  
\- Option to replay the game after it ends  
\- Handles invalid inputs gracefully

\## Installation

To run this game on your local machine, you need to have Python installed. Follow these steps to set up the game:

\### Clone the Repository:

\```bash  
git clone https://github.com/your-username/tic-tac-toe.git  
\```

\### Navigate to the Project Directory:

\```bash  
cd tic-tac-toe  
\```

\### Ensure Python is Installed:

Check if Python is installed by running:

\```bash  
python --version  
\```

If Python is not installed, download it from [python.org](https://www.python.org).

\## Usage

To start the Tic-Tac-Toe game, simply run the `main.py` file:

\```bash  
python3 main.py  
\```

If you are using Windows, you might need to use `python` instead of `python3`:

\```bash  
python main.py  
\```

\## How to Play

\- The game will start with a welcome message.  
\- Player 1 will be assigned the symbol "X" and Player 2 will be assigned the symbol "O".  
\- Players take turns to enter their moves by specifying the grid position (e.g., a1, b2, c3).  
\- The board is displayed after each move, showing the updated state.  
\- The game will check for a win or a draw after each move:  
\- If a player gets three of their symbols in a row, column, or diagonal, they win.  
\- If all cells are filled and no player has won, the game is a draw.  
\- After the game ends, players will be prompted to play again or exit.

\## Game Flow

1. **Start of the Game:** The game begins with a welcome message, and the board is displayed with empty cells.  
2. **Player Turn:** Players will be prompted to enter their move. The game will validate the move and update the board if it's valid.  
3. **Winning/Draw Condition:** The game will check for a win or draw after each move. If either condition is met, the game will end and display the result.  
4. **Replay Option:** After the game ends, players can choose to play again or exit the game.

\## Example Game Session

\```plaintext  
Starting the game...  
Welcome to Tic-Tac-Toe!  
a   b   c  
\-------------  
1 |   |   |   |  
\-------------  
2 |   |   |   |  
\-------------  
3 |   |   |   |  
\-------------

Player 1 (X), enter your move (e.g., a1, b2): a1  
a   b   c  
\-------------  
1 | X |   |   |  
\-------------  
2 |   |   |   |  
\-------------  
3 |   |   |   |  
\-------------

Player 2 (O), enter your move (e.g., a1, b2): b2  
...  
\```

\## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---