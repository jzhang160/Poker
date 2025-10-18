from Deck import Deck
from Player import Player

class Dealer:
    def deal(self, cards: int, deck: Deck, *args: Player):
        for _ in range(cards):
            for player in args:
                player.addCard(deck.pop())