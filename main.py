# Starting point of the Tic-Tac-Toe game
print("Starting the game...")

# Import the Game class from the lib directory
from lib.game import Game

if __name__ == "__main__":
    # Create an instance of the Game class
    game = Game()
    
    # Start the game by calling the play_game method
    game.play_game()

# Run the program with: python3 main.py
