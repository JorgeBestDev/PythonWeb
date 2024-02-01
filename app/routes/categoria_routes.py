from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app import db
from app.models.categoria import Categoria


bp = Blueprint('categoria', __name__)

@bp.route('/Categoria')
def index():
    Categoria = Categoria.query.all()
    return render_template('categoria/index.html', Categoria=Categoria)