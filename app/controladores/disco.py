from flask import Blueprint, render_template

from app.base import Session
from app.modelos.disco import Disco

detalle_disco_bp = Blueprint("detalle_disco", __name__)


@detalle_disco_bp.route("/disco/<int:id>")
def detalle_disco(id):
    disco = Session.get(Disco, id)
    return render_template("disco.html", detalle_disco=disco)
