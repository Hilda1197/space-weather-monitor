import sqlite3
import pandas as pd

def init_database():
    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS interruptions (
            event_id INTEGER PRIMARY KEY,
            event_time TEXT,
            duration_sec INTEGER,
            ky_index REAL,
            dst_index INTEGER,
            interruption_type TEXT
        )
    ''')
    
    df = pd.read_csv('data/sample_data.csv')
    df.to_sql('interruptions', conn, if_exists='replace', index=False)
    
    conn.commit()
    conn.close()
    print("数据库初始化完成！")

if __name__ == '__main__':
    init_database()