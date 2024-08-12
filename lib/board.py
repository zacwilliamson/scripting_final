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
        if self.is_valid_move(position):
            row, col = self.convert_position(position)
            self.grid[row][col] = symbol
            return True
        return False

    def is_valid_move(self, position):
        valid_inputs = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
        
        if position not in valid_inputs:
            return False

        row, col = self.convert_position(position)

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