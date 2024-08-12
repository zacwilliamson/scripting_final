class Board:
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
        self.columns = ['a', 'b', 'c']
        self.rows = ['1', '2', '3']

    def display_board(self):
        print("   a   b   c")
        print("  -------------")
        for i, row in enumerate(self.grid):
            row_display = f"{self.rows[i]} | {' | '.join(row)} |"
            print(row_display)
            print("  -------------")

    def update_board(self, position, symbol):
        row, col = self.convert_position(position)
        if self.is_valid_move(row, col):
            self.grid[row][col] = symbol
            return True
        return False

    def is_valid_move(self, row, col):
        return self.grid[row][col] == ' '

    def is_full(self):
        for row in self.grid:
            if ' ' in row:
                return False
        return True

    def convert_position(self, position):
        col = self.columns.index(position[0].lower())
        row = self.rows.index(position[1])
        return row, col