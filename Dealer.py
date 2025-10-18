from Deck import Deck
from Player import Player

class Dealer:
    def deal(self, numCards: int, deck: Deck, *args: Player) -> None:
        for _ in range(numCards):
            for player in args:
                player.add_card(deck.pop())

    def flop(self, deck: Deck):
        pass
        
    def turn(self):
        pass
        
    def river(self):
        pass