'''Kết nối CSDL'''
from pymysql import connect, cursors, Error


config = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "database": "blogs",
    "cursorclass": cursors.DictCursor
}

try:
    conn = connect(**config)
    cur = conn.cursor()
    print("Connected to database blogs:", conn.db.decode("UTF-8"))
except Error as e:
    print(e)

def set_log_post(title, content):
    '''
    Ghi thông tin về bài post vào CSDL vào bảng posts
    '''
    sql = '''
    INSERT INTO posts (title, content)
    VALUES (%s,%s)
    '''
    cur.execute(sql, (title, content))
    conn.commit()
    

def get_all_log_post():
    '''Lấy thông tin về danh sách các bài posts'''
    sql_game = '''
        SELECT * FROM posts ORDER BY create_at DESC'''

    cur.execute(sql_game)
    post =  cur.fetchall()
    return post
   
  
def get_one_log_post(post_id):
    '''Lấy thông tin về danh sách các bài posts'''
    sql = '''
        SELECT * FROM posts where post_id = %s'''

    cur.execute(sql,post_id)
    post =  cur.fetchone()
    return post
   
def update_post_info(title, content, post_id):
    sql = '''
        UPDATE posts
        SET title = %s,
            content = %s
        WHERE post_id = %s'''
    cur.execute(sql, (title, content,post_id))

    if cur.rowcount:
        conn.commit()
        return True
    else:
        return False