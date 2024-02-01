from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.categoria_has_producto import Categoria_has_producto
from app import db

bp = Blueprint('categoria_has_product', __name__)

@bp.route('/categoria_has_product')
def index():
    ChP = Categoria_has_producto.query.all()
    return render_template('categoria_has_product/index.html', ChP=ChP)