from flask import Blueprint, render_template

# from modelos.disco import Disco

# from app.base import Session

vendedor_bp = Blueprint("vendedor", __name__)


@vendedor_bp.route("/vendedor")
def vendedor():
    return render_template("vendedor.html")
