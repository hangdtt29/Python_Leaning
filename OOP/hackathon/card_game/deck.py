import random
from card import Card
from random import shuffle


class Deck:
    '''
    Class đại diện cho bộ bài, bao gồm 36 lá
    '''
    suits = ['♥','♦', '♣', '♠']
   
    ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9]

    def build(self):
        '''Tạo bộ bài'''
        self._cards = []
        for i in Deck.ranks:
            for j in Deck.suits:
                self._cards.append(Card(i,j))
        return self._cards
        
    @property
    def cards(self):
        return self._cards  

    def shuffle_card(self):
        '''Trộn bài'''
        shuffle(self.cards)
        

    def deal_card(self):
        '''Rút một lá bài từ bộ bài'''
        
        #card = random.choice(self.cards)
        if len(self.cards) == 0:
            return None
        card = self.cards.pop()                                                    
        return card  
