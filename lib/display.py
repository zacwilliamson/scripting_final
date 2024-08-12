class Display:
    def __init__(self):
        pass

    def show_welcome_message(self):
        print("Welcome to Tic-Tac-Toe!")

    def get_move(self, player):
        return input(f"{player.get_name()} ({player.get_symbol()}), enter your move (e.g., a1, b2): ")

    def show_invalid_move_message(self):
        print("Invalid move, try again.")

    def show_winner(self, player):
        print(f"Congratulations {player.get_name()}! You win!")

    def show_draw(self):
        print("It's a draw!")

    def ask_replay(self):
        return input("Do you want to play again? (yes/no): ").lower().startswith('y')
