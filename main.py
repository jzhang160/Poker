from Card import Card
from Deck import Deck
from Dealer import Dealer
from Player import Player
from Chip import Chip
import random

def start_fresh_deck() -> Deck:
    deck = Deck()
    deck.new_deck()
    deck.shuffle(3)
    deck.cut(random.randint(16, 36))
    return deck

def distribute_chip(players*):
    pass

def play():
    deck = start_fresh_deck()
    dealer = Dealer()
    player1 = Player("Jeff")
    player2 = Player("Hannah")
    dealer.deal(2, deck, player1, player2)
    


if __name__ == '__main__':
    play()

    print(player1.get_chip_value())
    player1.add_chip("WHITE")