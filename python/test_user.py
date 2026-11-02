import sqlite3

conn = sqlite3.connect("nexus.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO users
(username, password_hash)
VALUES
('Tilo', 'test')
""")

conn.commit()
conn.close()