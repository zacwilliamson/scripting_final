
from lib.board import Board
from lib.player import Player
from lib.detector import Detector
from lib.display import Display

class Game:
    def __init__(self):
        self.board = Board()
        self.display = Display()
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("Player 2", "O")
        self.detector = Detector(self.board)
        self.current_player = self.player1
        self.game_is_active = True

    def play_game(self):
        print("Ready to play!")
        # self.display.show_welcome_message()

        # while self.game_is_active:
        #     self.board.display_board()
        #     move = self.display.get_move(self.current_player)
            
        #     if self.board.update_board(move, self.current_player.get_symbol()):
        #         if self.detector.check_winner(self.current_player.get_symbol()):
        #             self.board.display_board()
        #             self.display.show_winner(self.current_player)
        #             self.game_is_active = False
        #         elif self.detector.check_draw():
        #             self.board.display_board()
        #             self.display.show_draw()
        #             self.game_is_active = False
        #         else:
        #             self.switch_player()
        #     else:
        #         self.display.show_invalid_move_message()

        # if self.display.ask_replay():
        #     self.reset_game()
        #     self.play_game()

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def reset_game(self):
        self.board = Board()
        self.detector = Detector(self.board)
        self.current_player = self.player1
        self.game_is_active = True