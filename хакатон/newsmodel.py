import sqlite3

class NewsModel():
    def __init__(self, connection):
        self.connection = connection
        
    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS news 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             title VARCHAR(100),
                             content VARCHAR(1000),
                             date VARCHAR(50),
                             user_id INTEGER,
                             deleted BOOLEAN
                             )''')
        cursor.close()
        self.connection.commit()
        
    def insert(self, title, content, date, user_id):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO news 
                          (title, content, date, user_id, deleted) 
                          VALUES (?, ?, ?, ?, ?)''', (title, content, date, str(user_id), str(False)))
        cursor.close()
        self.connection.commit()
        
    def get(self, news_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM news WHERE id = ?", (str(news_id),))
        row = cursor.fetchone()
        return row
    
    def get_all(self, user_id = None):
        cursor = self.connection.cursor()
        if user_id:
            cursor.execute("SELECT * FROM news WHERE user_id = ? AND deleted = ?",
                           (str(user_id), str(False)))
        else:
            cursor.execute("SELECT * FROM news")
        rows = cursor.fetchall()
        return rows
    
    def update(self, title, content, date, news_id):
        cursor = self.connection.cursor()
        cursor.execute('''UPDATE news
                          SET title = ?
                          WHERE id = ?''', (title, news_id,))
        cursor.execute('''UPDATE news 
                          SET content = ?
                          WHERE id = ?''', (content, news_id,)) 
        cursor.execute('''UPDATE news
                          SET date = ?
                          WHERE id = ?''', (date, news_id,))        
        cursor.close()
        self.connection.commit()         
    
    def delete(self, news_id):
        cursor = self.connection.cursor()
        cursor.execute('''UPDATE news
                          SET deleted = ?
                          WHERE id = ?''', (True, news_id,))
        cursor.close()
        self.connection.commit()    