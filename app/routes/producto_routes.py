from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app import db
from app.models.producto import Producto


bp = Blueprint('producto', __name__)

@bp.route('/producto')
def index():
    Producto = Producto.query.all()
    return render_template('authors/index.html', Producto=Producto)