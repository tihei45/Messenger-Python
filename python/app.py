import os
import sqlite3
from datetime import datetime, UTC
from flask import Flask, jsonify, render_template, request,session
from werkzeug.security import generate_password_hash,check_password_hash

DATABASE = "nexus.db"


app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)
app.secret_key = "3n9A!xP7m#K2qL8v@R5zY1sD"

def format_timestamp(timestamp_string):
    timestamp = datetime.fromisoformat(timestamp_string)
    timestamp = timestamp.replace(tzinfo=UTC)
    return timestamp.astimezone().strftime("%H:%M")


def create_database():

    sqlite3.connect(DATABASE)
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

def seed_database():
    import random

    sqlite3.connect(DATABASE)
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

if not os.path.exists("nexus.db"):
    create_database()
    seed_database()

conn = sqlite3.connect(
    "nexus.db",
    check_same_thread=False
)


@app.route("/")
def index():
    CURRENT_USER_ID = session.get("userid")

    if CURRENT_USER_ID is None:
        return render_template("login.html")

    return render_template("main.html", logged_in=True)



@app.route("/add", methods=["POST"])
def add():
    CURRENT_USER_ID = session.get("userid")
    if CURRENT_USER_ID is None:
        return "Nicht eingeloggt"
    data = request.get_json()

    chatid = data["chatid"]
    content = data["content"]

    cursor = conn.cursor()

    cursor.execute(
    """
    INSERT INTO messages
    (chatid, userid, content)
    VALUES
    (?, ?, ?)
    """,
    (chatid, CURRENT_USER_ID, content)
)

    conn.commit()

    return "Gespeichert"

@app.route("/create-chat", methods=["POST"])
def createChat():
    CURRENT_USER_ID = session.get("userid")
    if CURRENT_USER_ID is None:
        return "Nicht eingeloggt"
    cursor = conn.cursor()
    data = request.get_json()
    chatname = data["chatname"]
    cursor.execute(
        """
        INSERT INTO chats
        (chatname)
        VALUES
        (?)
        """,
        (chatname,)
    )
    chatid = cursor.lastrowid

    cursor.execute(
                    """
                    INSERT INTO chat_members
                    (chatid,userid)
                    VALUES
                    (?,?)
                    """,
                    (chatid,CURRENT_USER_ID)
                )



    users = data["user"]
    users = users.split(",")

    for user in users:
        user = user.strip()
        if user == "":
            continue
        cursor.execute(
            """ 
            SELECT userid
            FROM users
            WHERE username = ?
            """,
            (user,)
        )
        
        result = cursor.fetchone()
        if result is None:
            continue
        userId = result[0]
        if userId == session.get("userid"):
            if CURRENT_USER_ID is None:
                return "Nicht eingeloggt"
            continue
        cursor.execute(
                """
                INSERT INTO chat_members
                (chatid,userid)
                VALUES
                (?,?)
                """,
                (chatid,userId)
            )
    conn.commit()




    jsonID = {"chatid": chatid}


    return jsonify(jsonID)
    

@app.route("/messages/<chatid>", methods=["GET"])
def messages(chatid):    
    CURRENT_USER_ID = session.get("userid")
    if CURRENT_USER_ID is None:
        return "Nicht eingeloggt"

    messagesJson = []
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT
            messages.messageid,
            messages.chatid,
            messages.userid,
            users.username,
            messages.content,
            messages.created_at
        FROM messages
        JOIN users
            ON messages.userid = users.userid
        WHERE messages.chatid = ?
         """,
        (chatid,)
       
    )
    messagesValue = cursor.fetchall()
    for message in messagesValue:
        messagesJson.append({
            "messageid": message[0],
            "chatid": message[1],
            "userid": message[2],
            "username": message[3],
            "content": message[4],
            "timestamp": format_timestamp(message[5])
        })
    return jsonify(messagesJson)

@app.route("/chats", methods=["GET"])
def chats():

    CURRENT_USER_ID = session.get("userid")
    if CURRENT_USER_ID is None:
        return "Nicht eingeloggt"
    print(session.get("userid"))

    chatsjson = []
    cursor = conn.cursor()
    cursor.execute(
        """
        Select * FROM chats ORDER BY chatid DESC
            """,

        
    )
    chatValue = cursor.fetchall()
    for chats in chatValue:
        chatsjson.append({
            "chatid": chats[0],
            "chatname": chats[1]
        })
    return jsonify(chatsjson)



@app.route("/users", methods=["GET"])
def users():
    userjson = []
    cursor = conn.cursor()
    cursor.execute(
        """
        Select * FROM users
            """,
        )
    userValue = cursor.fetchall()
    for user in userValue:
        userjson.append(user[1])

    return jsonify(userjson)





@app.route("/register",  methods=["POST"])
def register():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    cursor = conn.cursor()
    cursor.execute(
            """
            Select * FROM users
            WHERE username = ?
                """,
            (username,)
            )
    result = cursor.fetchone()
    if result != None:
        return "Nutzer existiert bereits"
    password_hash = generate_password_hash(password)
    cursor.execute("""
        INSERT INTO users
        (username, password_hash)
        VALUES
        (?, ?)
        """, (username, password_hash))
    conn.commit()
    return "Registrierung erfolgreich"

@app.route("/register",  methods=["GET"])
def register_show():
    return render_template("register.html")






@app.route("/login",  methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    cursor = conn.cursor()
    cursor.execute(
            """
            Select userid,password_hash FROM users
            WHERE username = ?
                """,
            (username,)
            )
    
    result = cursor.fetchone()
    if result is None:
        return "Nuter existiert nicht"
    userid = result[0]
    password_hash = result[1]
    if check_password_hash(password_hash,password):
        session["userid"] = userid
        return "Erfolgreich Angemeldet"



    return "Falsches Passwort eingegeben"



@app.route("/login",  methods=["GET"])
def login_show():
    return render_template("login.html")



@app.route("/logout", methods=["POST"])
def logout():
    print("VORHER:", session.get("userid"))

    session.clear()

    print("NACHHER:", session.get("userid"))

    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)