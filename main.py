from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from config import *

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        # Obter dados do formulário
        username = request.form["username"]
        password = request.form["password"]

        # Conectar ao banco de dados
        connection = mysql.connector.connect(
            host=HOST, user=USER, password=PASSWORD, database=DATABASE
        )
        cursor = connection.cursor()

        # Validar o usuário
        query = "SELECT * FROM usuarios WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user is not None:
            # Usuário autenticado
            return redirect(url_for("home"))
        else:
            # Credenciais inválidas
            return render_template("login.html", error="Credenciais inválidas.")