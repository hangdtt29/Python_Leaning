class Player:
    '''
    Class đại diện cho mỗi người chơi

    Người chơi chỉ cần lưu tên, và các lá bài người chơi có
    '''
    count = 1

    def __init__(self, name):  # dễ
        self._name = name
        self._id = Player.count
        self._cards = []
        Player.count += 1

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    @property
    def cards(self):
        return self._cards

    @property 
    def infor(self):
        return "{:2} {}".format(self.id,self.name)

    @property
    def point(self):  # trung bình
        '''Tính điểm cho bộ bài'''
        sum_point = 0

        for i in range(0, len(self.cards)):
            rank = self.cards[i].rank
            sum_point += rank

        if sum_point % 10 == 0:
            return 10
        else:
            return sum_point % 10

    @property
    def biggest_card(self):
        '''
        Tìm lá bài lớn nhất
        Trong trường hợp điểm bằng nhau, sẽ so sánh lá bài lớn nhất để tìm ra người chiến thắng
        '''
        # Gọi hàm __gt__ so sánh các card đầu vào và trả ra kết quả max
        return max(self.cards)

    def add_card(self,card):
        '''Thêm một lá bài vào bộ (rút từ bộ bài)'''
        if card != None:
            self.cards.append(card)    

    def remove_card(self):
        '''Reset bộ bài khi chơi game mới'''
        self.cards.clear()

    def flip_card(self):
        '''Lật bài, hiển thị các lá bài'''
        return " ".join([str(c) for c in self.cards])
        # for i in self.cards:
        #     card_strs = " ".join(str(i))
        # return card_strs

    def __gt__(self,other):
        '''Player có lá bài to nhất'''
        if self.point > other.point:
            return True
        if self.point == other.point:
            if self.biggest_card > other.biggest_card:
                return True
            else:
                return False
        return False
        
        
