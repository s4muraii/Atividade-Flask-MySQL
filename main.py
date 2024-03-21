from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import connect
from config import *

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=3306)

connection = connect(host="127.0.0.1", user="root", password="", database="quitanda")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        try:
            connection = mysql.connector.connect(
                host=HOST, user=USER, password=PASSWORD, database=DATABASE
            )
            cursor = connection.cursor()

            query = "SELECT * FROM Usuarios WHERE usuario = %s AND senha = %s"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()

            if user is not None:
                return redirect(url_for("home"))
            else:
                return render_template("login.html", error="Credenciais inválidas.")
        except Exception:
            return render_template("login.html", error="Erro ao conectar ao banco de dados.")