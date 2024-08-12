from lib.board import Board
from lib.player import Player
from lib.detector import Detector
from lib.display import Display
import os
import sys

class Game:
    def __init__(self):
        """Initialize the game by setting up the board, players, and game state."""
        self.initialize_game()

    def initialize_game(self):
        """Set up the game components: board, players, and the detector."""
        self.board = Board()  # Initialize the game board
        self.display = Display()  # Initialize the display system
        self.player1 = Player("Player 1", "X")  # Create Player 1 with symbol 'X'
        self.player2 = Player("Player 2", "O")  # Create Player 2 with symbol 'O'
        self.detector = Detector(self.board)  # Initialize the detector for win/draw checks
        self.current_player = self.player1  # Set Player 1 to start the game
        self.game_is_active = True  # Set the game state to active

    def play_game(self):
        """Main game loop that continues until the game is over."""
        self.display.show_welcome_message()  # Show the welcome message at the start

        while self.game_is_active:
            self.play_turn()  # Play a turn in the game
            if not self.game_is_active:
                self.end_game()  # End the game if it's no longer active
        
        self.prompt_replay()  # Prompt the player to see if they want to replay

    def play_turn(self):
        """Handle a single turn in the game."""
        self.clear_screen()  # Clear the terminal screen for a fresh display
        self.board.display_board()  # Display the current state of the board
        move = self.display.get_move(self.current_player)  # Get the player's move
        
        if self.is_valid_move_and_update_board(move):
            if self.is_winning_move():
                self.end_game(winner=True)  # End the game if the move is a winning move
            elif self.is_draw():
                self.end_game(draw=True)  # End the game if it's a draw
            else:
                self.switch_player()  # Switch to the next player if the game continues
        else:
            self.display.show_invalid_move_message()  # Show an error message for an invalid move

    def is_valid_move_and_update_board(self, move):
        """Check if the move is valid and update the board accordingly."""
        return self.board.update_board(move, self.current_player.get_symbol())

    def is_winning_move(self):
        """Check if the current move wins the game."""
        return self.detector.check_winner(self.current_player.get_symbol())

    def is_draw(self):
        """Check if the game is a draw."""
        return self.detector.check_draw()

    def switch_player(self):
        """Switch the current player to the other player."""
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def end_game(self, winner=False, draw=False):
        """Handle the end of the game, displaying the result and stopping the game loop."""
        self.clear_screen()  # Clear the terminal screen before showing the final board
        self.board.display_board()  # Display the final state of the board
        if winner:
            self.display.show_winner(self.current_player)  # Show the winner's message
        elif draw:
            self.display.show_draw()  # Show the draw message
        self.game_is_active = False  # Set the game state to inactive

    def prompt_replay(self):
        """Prompt the player to see if they want to replay the game."""
        self.clear_screen()  # Clear the screen before asking for replay
        if self.display.ask_replay():
            self.reset_game()  # Reset the game state for a new game
            self.play_game()  # Start a new game

    def reset_game(self):
        """Reset the game state, reinitializing all components."""
        self.initialize_game()

    def clear_screen(self):
        """Clear the terminal screen based on the operating system."""
        if os.name == 'nt':  # For Windows systems
            os.system('cls')
        else:  # For macOS and Linux systems
            os.system('clear')
