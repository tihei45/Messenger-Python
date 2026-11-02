import sqlite3

conn = sqlite3.connect("nexus.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    userid INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS chats (
    chatid INTEGER PRIMARY KEY AUTOINCREMENT,
    chatname TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_members (
    chatid INTEGER NOT NULL,
    userid INTEGER NOT NULL,
    PRIMARY KEY (chatid, userid)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    messageid INTEGER PRIMARY KEY AUTOINCREMENT,
    chatid INTEGER NOT NULL,
    userid INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Datenbank erstellt")