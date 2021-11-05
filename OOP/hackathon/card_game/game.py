from deck import Deck
from player import Player
import db
import sys

class Game:
    '''
    Class chứa các chức năng chính của game

    Game chứa danh sách người chơi, và bộ bài
    '''
    min_player = 2
    max_player = 12
    number_of_cards = 3

    def __init__(self):
        self._deck = Deck()
        self._member = []
        self.choice = {
            "1" : self.list_players,
            "2" : self.add_player,
            "3" : self.remove_player,
            "4" : self.deal_card,
            "5" : self.flip_card,
            "6" : self.last_game,
            "7" : self.history,
            "8" : self.quite

        }


    @property
    def deck(self):
        return self._deck
            
    @property
    def member(self):
       return self._member

    def setup(self):
        '''Khởi tạo trò chơi, nhập số lượng và lưu thông tin người chơi'''
        member = int(input("Có bao nhiêu người muốn chơi: ? "))
        for i in range(1, member + 1):
            name = input("Tên người chơi {} : ".format(i))
            self.member.append(Player(name))
        return self.member
    
    def guide(self):
        '''Hiển thị menu chức năng/hướng dẫn chơi'''
        print(f"1. Danh sách người chơi ({len(self.member)})")
        print(f"2. Thêm người chơi ()")
        print(f"3. Loại người chơi ()")
        print(f"4. Chia bài")
        print(f"5. Lật bài")
        print(f"6. Xem lại game vừa chơi")
        print(f"7. Xem lại lịch sử game vừa chơi hôm nay")
        print(f"8. Dừng trò chơi")
        

    def list_players(self):
        '''Hiển thị danh sách người chơi'''
        print(f"ID Name")
        for player in self.member:
            print(player.infor)
        

    def add_player(self):
        '''Thêm một người chơi mới'''

        name = input("Tên người chơi thứ {}: ".format(len(self.member) + 1))
        self.member.append(Player(name))
        return self.member

    def remove_player(self):
        '''
        Loại một người chơi
        Mỗi người chơi có một ID (có thể lấy theo index trong list)
        '''
        print(self.list_players())
        id = int(input("Nhập vào id người chơi: "))
        player = self.member[id - 1] 
        self.member.remove(player)
        

    def deal_card(self):
        '''Chia bài cho người chơi'''
        print("Chia bài cho người chơi thôi =)")
        # reset quân bài người chơi
        for player in self.member:
            player.remove_card()
            
        self.deck.build()
        self.deck.shuffle_card()
        for i in range(Game.number_of_cards):
            for player in self.member:
               card_for_player = self.deck.deal_card()
               player.add_card(card_for_player)

              
    def flip_card(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
        print("Lật bài chơi thôi anh em")
        win_player = max(self.member)

        for player in self.member:
            print(f"Tên: {player.name}: {player.flip_card()} Tổng điểm: {player.point} Quân bài lớn nhất: {player.biggest_card}")
        print(f"Người chiến thắng: {win_player.name}")

        player_db = [{"player": p.name, "cards": p.flip_card(), "point" : p.point, "biggest_card": p.biggest_card} for p in self.member]
        db.log(win_player.name,player_db)
        
        

    def last_game(self):
        '''Lấy thông tin về game gần nhất từ cả 2 bảng games và logs'''
        print("Thông tin ván chơi gần nhất nhé ae")
        game, players = db.get_last_game()

        print('ID của ván game',game["game_id"])

        for player in players:
           print(f'Tên: {player["player"]}: {player["cards"]} Tổng điểm: {player["point"]} Quân bài lớn nhất: {player["biggest_card"]}')
        print(f'Người chiến thắng: {game["winner"]}')
    

    def history(self):
        '''Lấy thông tin về lịch sử chơi
        Bao gồm tổng số game đã chơi, số game chiến thắng ứng với mỗi người chơi'''
        print("Lịch sử chơi bài hôm nay:")
        total, infor_historyGame = db.history()
        print(f'Hôm nay chơi tổng số ván: {total["total"]} ')
        for games in infor_historyGame:
            print(f'Tên người chiến thắng: {games["winner"]} | Số ván thắng: {games["numberofGame"]}')
    
    

    def quite(self):
        print("Quite game")
        sys.exit()

    def run(self):
        self.setup()
        while True:
            self.guide()
            select = input("> ")
            choise = self.choice.get(select)
            if choise:
                choise()
            else:
                print("Vui lòng chọn lại yêu cầu: ")



