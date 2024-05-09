import sqlite3
import os

def db_conn():
    try:
        conn = sqlite3.connect('mydatabase.db')
        return conn
    except Exception as e:
        print("An error occurred while connecting to the database:", e)
        return None

def db_create(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS file_records (
                id INTEGER PRIMARY KEY,
                filename TEXT
            )
        ''')
        conn.commit()
    except Exception as e:
        print("An error occurred while creating the table:", e)

def db_insert(conn, filename):
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO file_records (filename) VALUES (?)', (filename,))
        conn.commit()
    except Exception as e:
        print("An error occurred while inserting data into the table:", e)

def db_select(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM file_records')
        rows = cursor.fetchall()
        print("Table Contents:")
        for row in rows:
            print(row)
    except Exception as e:
        print("An error occurred while selecting data from the table:", e)

if __name__ == '__main__':
    # 连接数据库
    conn = db_conn()
    if conn:
        # 创建表格
        db_create(conn)
         # 获取out文件夹中的文件名
        folder_path = "out"
        file_names = os.listdir(folder_path)

        # 插入数据
        for file_name in file_names:
            db_insert(conn, file_name)

        # 查询数据并输出到屏幕
        db_select(conn)

        conn.close()
    else:
        print("Failed to connect to the database.")