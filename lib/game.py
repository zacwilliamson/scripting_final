from lib.board import Board
from lib.player import Player
from lib.detector import Detector
from lib.display import Display

class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.board = Board()
        self.display = Display()
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("Player 2", "O")
        self.detector = Detector(self.board)
        self.current_player = self.player1
        self.game_is_active = True

    def play_game(self):
        self.display.show_welcome_message()

        while self.game_is_active:
            self.play_turn()
            if not self.game_is_active:
                self.end_game()
        
        self.prompt_replay()

    def play_turn(self):
        self.board.display_board()
        move = self.display.get_move(self.current_player)
        
        if self.is_valid_move_and_update_board(move):
            if self.is_winning_move():
                self.end_game(winner=True)
            elif self.is_draw():
                self.end_game(draw=True)
            else:
                self.switch_player()
        else:
            self.display.show_invalid_move_message()

    def is_valid_move_and_update_board(self, move):
        return self.board.update_board(move, self.current_player.get_symbol())

    def is_winning_move(self):
        return self.detector.check_winner(self.current_player.get_symbol())

    def is_draw(self):
        return self.detector.check_draw()

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def end_game(self, winner=False, draw=False):
        self.board.display_board()
        if winner:
            self.display.show_winner(self.current_player)
        elif draw:
            self.display.show_draw()
        self.game_is_active = False

    def prompt_replay(self):
        if self.display.ask_replay():
            self.reset_game()
            self.play_game()

    def reset_game(self):
        self.initialize_game()

if __name__ == "__main__":
    game = Game()
    game.play_game()