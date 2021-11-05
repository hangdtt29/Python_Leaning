class Card:
    '''
    Class đại diện cho mỗi lá bài

    Mỗi lá bài bao gồm rank ('A', 2, 3, 4, 5, 6, 7, 8, 9) và suit ('♠', '♣', '♦', '♥')
    '''

    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        if self._rank == "A":
            return 1
        else:
            return self._rank

    @property
    def suit(self):
        points = {'♥': 4, '♦': 3, '♣': 2, '♠': 1}
        point_suit = points.get(self._suit)
        return point_suit

    def __str__(self):
        '''Hiển thị lá bài'''
        card_value = f"{self.rank}{self._suit}"
        return card_value

    def __gt__(self, other):
        '''So sánh 2 lá bài
           So sánh theo chất trước, sau đó theo điểm quân bài
           ''' 
        if self.suit > other.suit:
            return True
        if self.suit == other.suit:
            if self.rank > other.rank:
                return True
            else:
                return False
        return False

card1 = Card(7,'♠')
print(card1)
# card2 = Card(4,'♥')
# card3 = Card(9,'♣')
# print(max(card1,card2,card3))