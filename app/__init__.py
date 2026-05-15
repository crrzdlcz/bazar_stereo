from flask import Flask, render_template

from app.controladores.disco import detalle_disco_bp
from app.controladores.discos import discos_bp
from app.controladores.subastas import subasta_bp
from app.controladores.vendedor import vendedor_bp

from .controladores.rutas import main_bp

app = Flask(__name__, template_folder="templates", static_folder="static")

app.register_blueprint(main_bp)
app.register_blueprint(discos_bp)
app.register_blueprint(subasta_bp)
app.register_blueprint(detalle_disco_bp)
app.register_blueprint(vendedor_bp)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error_404.html")


if __name__ == "__main__":
    app.run(debug=True)
