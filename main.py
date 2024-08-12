print("Starting the game...")

from lib.game import Game  # Import the Game class from the lib folder

if __name__ == "__main__":
    game = Game()  # Create an instance of the Game class
    game.play_game()  # Start the game