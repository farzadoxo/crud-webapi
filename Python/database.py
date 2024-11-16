import sqlite3



class Database:
    conn = sqlite3.connect('user_database.db' , check_same_thread=False)
    cur = conn.cursor()




def init_database():
    Database.cur.execute("""CREATE TABLE IF NOT EXISTS info (
                         NationalCode TEXT PRIMARY KEY ,
                         FirstName TEXT NOT NULL ,
                         LastName TEXT NOT NULL,
                         Age INTEGER NOT NULL,
                         Country TEXT NOT NULL,
                         Gender BOOLEAN NOT NULL)
                         """)
    


if __name__ == "__main__" :
    init_database()