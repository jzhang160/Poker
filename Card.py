class Card:
    def __init__(self, value, suit):
        if value < 10:
            self.value = value + 1
        else:
            match value:
                case 10:
                    self.value = "Jack"
                case 11:
                    self.value = "Queen"
                case 12:
                    self.value = "King"
        self.suit = suit

    def __str__(self):
        return f"{self.value} of {self.suit}s"
    
    def __eq__(self, other):
        if self.value == other.value and self.suit == other.suit:
            return True
        return False