class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, player):
        """Default item use method – should be overridden by specific item types."""
        print(f"{self.name} nemá žádný speciální efekt.")