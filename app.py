from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

generos = [
    "Rock",
    "Pop",
    "Electronica",
    "Jazz",
    "Country",
    "Metal",
    "EDM",
    "No binario",
]  # Estos deben extraerse de la bd.
elementos = 0


# <--- Rutas --->
# Estas funciones definen las rutas de nuestra pagina web.
@app.route("/")
def inicio():
    return render_template("index.html")


# Ruta de las subastas (Solo los discos que son subastas)
@app.route("/subastas")
def subastas():
    return render_template("subastas.html")


# Ruta de los discos (no subastas)
@app.route("/discos")
def discos():
    return render_template(
        "discos.html", lista_generos=generos, elementos_pagina=elementos
    )


# Ruta de los discos en oferta (no subastas, discos en gral.)
@app.route("/ofertas")
def ofertas():
    return render_template(
        "ofertas.html", lista_generos=generos, elementos_pagina=elementos
    )


# Ruta para el inicio de sesión.
@app.route("/login")
def login():
    return render_template("login.html")


# Ruta para la cuenta del usuario
@app.route("/mi_cuenta")
def mi_cuenta():
    return render_template("mi_cuenta.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error_404.html")


if __name__ == "__main__":
    app.run(debug=True)
