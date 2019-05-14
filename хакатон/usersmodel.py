import sqlite3

class UsersModel():
    def __init__(self, connection):
        self.connection = connection
        
    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             username VARCHAR(50),
                             name VARCHAR(50),
                             surname VARCHAR(50),
                             status VARCHAR(50),
                             password_hash VARCHAR(250),
                             token VARCHAR(500))''')
        cursor.close()
        self.connection.commit()
     
    def insert(self, username, name, surname, password_hash):
        cursor = self.connection.cursor()
        status = 'unblocked'
        photo_url = 'https://gramps-project.org/wiki/images/2/22/Macos_200x200.png'
        cursor.execute('''INSERT INTO users 
                          (username, name, surname, status, password_hash, token) 
                          VALUES (?,?,?,?,?,?)''', (username, name, surname, status, password_hash, photo_url))
        cursor.close()
        self.connection.commit()     
       
    def update_status(self, status, user_id):
        cursor = self.connection.cursor()
        cursor.execute('''UPDATE users 
                          SET status = ? 
                          WHERE id = ?''', (status, user_id,))
        cursor.close()
        self.connection.commit()
        
    def add_token(self, url, user_id):
        cursor = self.connection.cursor()
        cursor.execute('''UPDATE users 
                          SET token = ? 
                          WHERE id = ?''', (url, user_id,))
        cursor.close()
        self.connection.commit()        
        
    def exists(self, username, password_hash):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password_hash = ?", (username, password_hash))
        row = cursor.fetchone()
        return (True, row[0], row[4]) if row else (False,)
    
    def password_check(self, username):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username, ))
        row = cursor.fetchone()
        try:
            return row[5]
        except:
            return 'no'
    
    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (str(user_id),))
        row = cursor.fetchone()
        return row
    
    def block(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute('''UPDATE users 
                          SET status = ? 
                          WHERE id = ?''', ('blocked', user_id,))
        cursor.close()
        self.connection.commit()          
    
    def unblock(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute('''UPDATE users 
                          SET status = ? 
                          WHERE id = ?''', ('', user_id,))
        cursor.close()
        self.connection.commit()       
    
    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return rows    