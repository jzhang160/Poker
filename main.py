from Card import Card
from Deck import Deck
from Dealer import Dealer
from Player import Player
import random

if __name__ == '__main__':
    deck = Deck()
    deck.new_deck()
    deck.shuffles(3)
    deck.cut(random.randint(16,36))

    print(deck)



    dealer = Dealer()
    player1 = Player("Jeff")
    player2 = Player("Hannah")
    dealer.deal(5, deck, player1, player2)