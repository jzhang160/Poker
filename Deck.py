from Card import Card
import random

class Deck:
    def __init__(self, cards: list[Card] = None):
        if cards == None:
            self.new_deck()
        else:
            self.deck = cards
    
    def __str__(self):
        s = '------------------------\n'
        for n in self.deck:
            s += str(n) + '\n'
        s += '------------------------\n'
        return s
    
    def __len__(self):
        return len(self.deck)
    
    def new_deck(self):
        cards = []
        for suit in ['Spade', 'Heart', 'Club', 'Diamond']:
            for value in range(13):
                cards.append(Card(value, suit))
        self.deck = cards
    
    def random_deck(self):
        cards = []
        slots = 52
        while slots > 0:
            suit = random.choice(['Spade', 'Heart', 'Club', 'Diamond'])
            value = random.randint(0,12)
            card = Card(value, suit)
            if card not in cards:
                cards.append(card)
                slots -= 1
        self.deck = cards
    
    def shuffles(self, x):
        for n in range(x):
            self.shuffle()
        return self

    def shuffle(self):
        newDeck = []
        top =  self.deck[26:]
        bot = self.deck[0:26]
        for n in range(26):
            newDeck.append(top[n])
            newDeck.append(bot[n])
        self.deck = newDeck
        return self
    
    def cut(self, x):
        top = self.deck[x:]
        bot = self.deck[:x]
        self.deck = top + bot
        return self
    
    def pop(self):
        if len(self.deck) > 0:
            return self.deck.pop()
        else:
            print("No more cards in the deck!")