import sqlite3
import random

conn = sqlite3.connect("nexus.db")
cursor = conn.cursor()

# Alte Daten löschen
cursor.execute("DELETE FROM messages")
cursor.execute("DELETE FROM chat_members")
cursor.execute("DELETE FROM chats")
cursor.execute("DELETE FROM users")

cursor.execute("DELETE FROM sqlite_sequence WHERE name='users'")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='chats'")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='messages'")

# User
users = [
    "Tilo", "Max", "Anna", "Sophie", "Ben",
    "Tom", "Lisa", "Paul", "Emma", "Noah",
    "Leon", "Mia", "Finn", "Lukas", "Lea",
    "Jonas", "Marie", "Tim", "Sarah", "Felix"
]

for user in users:
    cursor.execute("""
    INSERT INTO users
    (username, password_hash)
    VALUES
    (?, ?)
    """, (user, "test"))

# Chats
for i in range(1, 11):
    cursor.execute("""
    INSERT INTO chats
    (chatname)
    VALUES
    (?)
    """, (f"Chat {i}",))

# Mitgliedschaften
for chatid in range(1, 11):

    member_count = random.randint(3, 8)

    members = random.sample(range(1, 21), member_count)

    for userid in members:
        cursor.execute("""
        INSERT INTO chat_members
        (chatid, userid)
        VALUES
        (?, ?)
        """, (chatid, userid))

# Nachrichten
texts = [
    "Hallo zusammen",
    "Was geht?",
    "Hat jemand Zeit?",
    "Das läuft!",
    "Sieht gut aus",
    "Okay",
    "Perfekt",
    "Bin gleich da",
    "Lass uns anfangen",
    "Klingt super",
    "Das funktioniert",
    "Ich teste gerade",
    "Cool",
    "Gute Idee",
    "Danke"
]

for _ in range(200):

    chatid = random.randint(1, 10)

    cursor.execute("""
    SELECT userid
    FROM chat_members
    WHERE chatid = ?
    """, (chatid,))

    members = cursor.fetchall()

    if not members:
        continue

    userid = random.choice(members)[0]
    text = random.choice(texts)

    cursor.execute("""
    INSERT INTO messages
    (chatid, userid, content)
    VALUES
    (?, ?, ?)
    """, (chatid, userid, text))

conn.commit()
conn.close()

print("Testdaten erstellt")