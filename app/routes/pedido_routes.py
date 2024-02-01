from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app import db
from app.models.pedido import Pedido


bp = Blueprint('pedido', __name__)

@bp.route('/pedido')
def index():
    Pedido = Pedido.query.all()
    return render_template('pedido/index.html', Pedido=Pedido)