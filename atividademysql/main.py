from flask import Flask, render_template, request, redirect, url_for
from mysql.connector import connect
from config import *

app = Flask(__name__)

if __name__ == "__main__":
    connection = connect(host="127.0.0.1", user="root", password="", database="quitanda")
    
    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "GET":
            return render_template("login.html")
        elif request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]

            try:

                cursor = connection.cursor()

                query = "SELECT * FROM Usuarios WHERE usuario = %s AND senha = %s"
                cursor.execute(query, (username, password))
                user = cursor.fetchone()

                if user is not None:
                    return redirect(url_for("home"))
                else:
                    return render_template("./Templates/login.html", error="Credenciais inválidas.")
            except Exception:
                return render_template("./Templates/login.html", error="Erro ao conectar ao banco de dados.")

    cursor = connection.cursor()
    cursor.close()
    connection.close()