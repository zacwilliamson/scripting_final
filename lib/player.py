class Player:
    def __init__(self, name, symbol):
        """Initialize a player with a name and a symbol ('X' or 'O')."""
        self.name = name  # Set the player's name
        self.symbol = symbol  # Set the player's symbol

    def get_name(self):
        """Return the player's name."""
        return self.name

    def get_symbol(self):
        """Return the player's symbol."""
        return self.symbol
