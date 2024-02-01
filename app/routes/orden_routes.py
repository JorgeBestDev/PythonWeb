from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app import db
from app.models.orden import Orden


bp = Blueprint('orden', __name__)

@bp.route('/Orden')
def index():
    Orden = Orden.query.all()
    return render_template('orden/index.html', Orden=Orden)