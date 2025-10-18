from Card import Card

class Player:
    def __init__(self, name, hand = None):
        self.name = name
        if hand == None:
            self.hand = []
        else:
            self.hand = hand

    def getName(self):
        return self.name

    def showHand(self):
        if len(self.hand) > 0:
            for n in self.hand:
                print(n)
        else:
            print("Empty Hand!")
    
    def addCard(self, card: Card):
        self.hand.append(card)

