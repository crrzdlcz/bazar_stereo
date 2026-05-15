from flask import Blueprint, render_template

from app.base import Session
from app.modelos.disco import Disco

discos_bp = Blueprint("discos", __name__)


@discos_bp.route("/discos")
def discos():
    discos = Session.query(Disco).filter(Disco.estado == 0).all()
    return render_template("discos.html", discos=discos)
