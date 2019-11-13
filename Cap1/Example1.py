# -*- coding: latin-1 -*-

import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck():
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades hearts diamonds clubs'.split() # 'spades diamonds clubs hearts'

    def __init__(self): 
        self._cards = [Card(rank, suit) for suit in self.suits
        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __repr__(self):
        print(self._cards[0], type(self._cards[0]))
        return "self._cards"

Deck = FrenchDeck() # Creamos un objeto baraja, Create a deck object
# print(Deck[0]) 
print(Deck[0::13]) 
