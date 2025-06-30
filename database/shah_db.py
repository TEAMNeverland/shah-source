import sqlite3

conn = sqlite3.connect("shah_full.db", check_same_thread=False)
cur = conn.cursor()

# مثال فقط لجداول الترحيب والرتب
cur.execute("""
CREATE TABLE IF NOT EXISTS welcome_settings (
    chat_id INTEGER PRIMARY KEY,
    welcome_text TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS ranks (
    user_id INTEGER,
    chat_id INTEGER,
    rank TEXT,
    PRIMARY KEY (user_id, chat_id)
)
""")

conn.commit()
conn.close()
