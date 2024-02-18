from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.usuario_has_orden import Usuario_has_Orden
from app import db

bp = Blueprint('usuario_has_orden', __name__)

@bp.route('/usuario_has_orden')
def index():
    UhO = Usuario_has_Orden.query.all()
    return render_template('categoria_has_product/index.html', UhO=UhO)