from flask import Blueprint, render_template

from app.base import Session
from app.modelos.disco import Disco

subasta_bp = Blueprint("subastas", __name__)


@subasta_bp.route("/subastas")
def subastas():
    discos_subastados = Session.query(Disco).filter(Disco.estado == 1).all()
    return render_template("subastas.html", subastas=discos_subastados)
