# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 19:24:25 2021

@author: vigilbushido
"""
import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class SpanishDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
def main():
    soda_card = Card('7', 'diamonds')
    print(soda_card)
    
    deck = SpanishDeck()
    print(len(deck))
    
    print(choice(deck))
    print(choice(deck))
if __name__ == "__main__":
    main()
    