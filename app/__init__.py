from flask import Flask
from flask.templating import render_template

from .controladores.rutas import main_bp

app = Flask(__name__, template_folder="templates", static_folder="static")

app.register_blueprint(main_bp)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error_404.html")


if __name__ == "__main__":
    app.run(debug=True)
