class Detector:
    def __init__(self, board):
        self.board = board

    def check_winner(self, symbol):
        # Check rows, columns, and diagonals
        return self.check_rows(symbol) or self.check_columns(symbol) or self.check_diagonals(symbol)

    def check_draw(self):
        return self.board.is_full() and not self.check_winner('X') and not self.check_winner('O')

    def check_rows(self, symbol):
        for row in self.board.grid:
            if all([cell == symbol for cell in row]):
                return True
        return False

    def check_columns(self, symbol):
        for col in range(3):
            if all([self.board.grid[row][col] == symbol for row in range(3)]):
                return True
        return False

    def check_diagonals(self, symbol):
        if all([self.board.grid[i][i] == symbol for i in range(3)]):
            return True
        if all([self.board.grid[i][2-i] == symbol for i in range(3)]):
            return True
        return False