class Detector:
    def __init__(self, board):
        """Initialize the detector with a reference to the game board."""
        self.board = board  # Keep a reference to the game board

    def check_winner(self, symbol):
        """Check if the current player has won the game."""
        # Check rows, columns, and diagonals for a winning combination
        return self.check_rows(symbol) or self.check_columns(symbol) or self.check_diagonals(symbol)

    def check_draw(self):
        """Check if the game is a draw."""
        # A draw occurs if the board is full and there's no winner
        return self.board.is_full() and not self.check_winner('X') and not self.check_winner('O')

    def check_rows(self, symbol):
        """Check each row to see if the current player has won."""
        for row in self.board.grid:
            if all([cell == symbol for cell in row]):  # Check if all cells in a row match the symbol
                return True
        return False

    def check_columns(self, symbol):
        """Check each column to see if the current player has won."""
        for col in range(3):
            if all([self.board.grid[row][col] == symbol for row in range(3)]):  # Check if all cells in a column match
                return True
        return False

    def check_diagonals(self, symbol):
        """Check the two diagonals to see if the current player has won."""
        # Check the diagonal from top-left to bottom-right
        if all([self.board.grid[i][i] == symbol for i in range(3)]):
            return True
        
        # Check the diagonal from top-right to bottom-left
        if all([self.board.grid[i][2-i] == symbol for i in range(3)]):
            return True
        
        return False
