class Board:
    def __init__(self):
        """Initialize the 3x3 Tic-Tac-Toe grid and define columns and rows."""
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]  # Create a 3x3 grid filled with spaces
        self.columns = ['a', 'b', 'c']  # Define the column labels
        self.rows = ['1', '2', '3']  # Define the row labels

    def display_board(self):
        """Display the current state of the board in a visually appealing format."""
        print("   a   b   c")
        print("  -------------")
        for i, row in enumerate(self.grid):
            row_display = f"{self.rows[i]} | {' | '.join(row)} |"  # Format each row for display
            print(row_display)
            print("  -------------")

    def update_board(self, position, symbol):
        """Update the board with the player's move if it's valid."""
        if self.is_valid_move(position):
            row, col = self.convert_position(position)  # Convert position like 'a1' to grid indices
            self.grid[row][col] = symbol  # Place the player's symbol on the grid
            return True
        return False

    def is_valid_move(self, position):
        """Check if the move is valid (within bounds and on an empty space)."""
        valid_inputs = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']  # List of valid positions
        
        if position not in valid_inputs:
            return False  # Return False if the position is not valid

        row, col = self.convert_position(position)  # Convert position to grid indices

        return self.grid[row][col] == ' '  # Return True if the cell is empty

    def is_full(self):
        """Check if the board is full (used to determine a draw)."""
        for row in self.grid:
            if ' ' in row:  # If there's an empty space, the board is not full
                return False
        return True

    def convert_position(self, position):
        """Convert a position like 'a1' into grid indices."""
        col = self.columns.index(position[0].lower())  # Convert column letter to index
        row = self.rows.index(position[1])  # Convert row number to index
        return row, col
