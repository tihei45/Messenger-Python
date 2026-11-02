from flask import Flask, render_template,request,jsonify
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
import mariadb

conn = mariadb.connect(
    host="localhost",
    user="root",
    password="",
    database="nexus"
)

print("Verbunden")


app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


@app.route("/")
def index():
    return render_template("main.html")




@app.route("/add", methods=["POST"])
def add():

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
        (chatid, 1, content)
    )

    conn.commit()

    return "Gespeichert"

@app.route("/create-chat", methods=["POST"])
def createChat():
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
                    (chatid,1)
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
        if userId == 1:
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
            "timestamp": message[5].strftime("%H:%M")
        })
    return jsonify(messagesJson)

@app.route("/chats", methods=["GET"])
def chats():
    chatsjson = []
    cursor = conn.cursor()
    cursor.execute(
        """
        Select * FROM chats
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

if __name__ == "__main__":
    app.run(debug=True)