from Card import Card
from Chip import Chip

class Player:
    def __init__(self, name: str, hand: list[Card] = None):
        self.chips = {  "WHITE": 0,
                        "RED": 0,
                        "BLUE": 0,
                        "GREEN": 0,
                        "BLACK": 0,
                        "PURPLE": 0 }
        self.name = name
        if hand == None:
            self.hand = []
        else:
            self.hand = hand

    def get_name(self):
        return self.name

    def show_hand(self):
        if len(self.hand) > 0:
            for n in self.hand:
                print(n)
        else:
            print("Empty Hand!")
    
    def add_card(self, card: Card):
        self.hand.append(card)

    def add_chip(self, color):
        if color in Chip.__members__:
            self.chips[color] += 1

    def get_chip_value(self):
        total_value = 0
        for key, value in self.chips.items():
            total_value += Chip[key].value * value
        return total_value

