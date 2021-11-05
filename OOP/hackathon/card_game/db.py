'''Kết nối CSDL'''
from pymysql import connect, cursors, Error


config = {
    "host": "localhost",
    "user": "root",
    "password": "Mysql209*",
    "database": "game_log",
    "cursorclass": cursors.DictCursor
}

try:
    conn = connect(**config)
    cur = conn.cursor()
    print("Connected to database game_log:", conn.db.decode("UTF-8"))
except Error as e:
    print(e)

def log(winner,player):
    '''
    Ghi thông tin về game vào CSDL và 2 bảng games và logs

    Bảng games gồm tên người chiến thắng

    Bảng logs gồm danh sách người chơi, bộ bài, điểm và lá bài lớn nhất tương ứng với game

    Chú ý, sau khi INSERT vào games, có thể lấy id của game vừa tạo với cursor.lastrowid
    '''
    sql = '''
    INSERT INTO games (winner)
    VALUES (%s)
    '''
    cur.execute(sql, winner)
    game_id = cur.lastrowid
    sql = f'''INSERT INTO logs (game_id, player, cards, point, biggest_card)
                            VALUES ({game_id}, %(player)s,%(cards)s,%(point)s,%(biggest_card)s)'''
                
    cur.executemany(sql,player)
    conn.commit()


def get_last_game():
    '''Lấy thông tin về game gần nhất từ cả 2 bảng games và logs'''
    sql_game = '''
        SELECT * FROM games ORDER BY play_at DESC'''
        # Truyền args cho params
    cur.execute(sql_game)
    game =  cur.fetchone()
    sql_player = f'''SELECT * FROM logs WHERE game_id = {game['game_id']}'''
    cur.execute(sql_player)
    players = cur.fetchall()
    return game,players
   
  
def history():
    '''
    Lấy thông tin về lịch sử chơi

    Bao gồm tổng số game đã chơi, số game chiến thắng ứng với mỗi người chơi (sử dụng GROUP BY và các hàm tổng hợp)
    '''

    sql_total_game = '''SELECT COUNT(game_id) as total
            FROM games 
            WHERE DATE(games.play_at) = CURDATE()'''
    cur.execute(sql_total_game)
    total = cur.fetchone()
    sql_history = '''SELECT COUNT(game_id) as numberofGame, winner 
            FROM games 
            WHERE DATE(games.play_at) = CURDATE()
            GROUP BY winner'''
    
    cur.execute(sql_history)
    infor_games = cur.fetchall()

    return total, infor_games