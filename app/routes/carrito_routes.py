from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.carrito import Carrito
from app import db

bp = Blueprint('usuario_has_orden', __name__)

@bp.route('/carrito')
def index():
    carrito = Carrito.query.all()
    return render_template('categoria_has_product/index.html', Carrito=carrito)