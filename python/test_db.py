import sqlite3

conn = sqlite3.connect("nexus.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")

print(cursor.fetchall())

conn.close()