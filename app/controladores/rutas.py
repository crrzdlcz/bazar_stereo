from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)


# <-- Rutas -->
@main_bp.route("/")
def inicio():
    return render_template("index.html")


@main_bp.route("/discos")
def discos():
    return render_template("discos.html")


@main_bp.route("/subastas")
def subastas():
    return render_template("subastas.html")


@main_bp.route("/micuenta")
def mi_cuenta():
    return render_template("mi_cuenta.html")


@main_bp.route("/disco")
def disco():
    return render_template("disco.html")


@main_bp.route("/carrito")
def carrito():
    return render_template("carrito.html")


# Para el vendedor
@main_bp.route("/extra/vendedor")
def vendedor():
    return render_template("vendedor.html")
