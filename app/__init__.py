from flask import Flask
import os
import socket
import mysql.connector

app = Flask(__name__)

@app.route("/hello")
def helloworld():
    return "Hello World with Python Flask!"

@app.route('/')
def hello():
    html = "<h3>Hello World from {hostname}!</h3>"
    html += "<h3>Your random word is: {random_word}</h3>"

    db = mysql.connector.connect(
        host=os.getenv("MYSQL_SERVICE_HOST", "localhost"),
        port=int(os.getenv("MYSQL_SERVICE_PORT", 3306)),  # Default to 3306 if not set
        user=os.getenv("MYSQL_DB_USER", "admin"),  # Change if using a different user
        passwd=os.getenv("MYSQL_DB_PASSWORD"),
        database="pyapplicationdb",
        auth_plugin="mysql_native_password"
    )

    cursor = db.cursor()
    cursor.execute("SELECT word FROM random_words ORDER BY RAND() LIMIT 1;")
    res = cursor.fetchall()

    return html.format(random_word=res[0][0], hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
