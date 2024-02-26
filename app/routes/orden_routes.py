from flask import Blueprint, render_template, request, redirect, url_for, jsonify,flash
from app import db
from app.models.orden import Orden


bp = Blueprint('orden', __name__)

@bp.route('/Orden')
def index():
    flash('Pedidos listados correctamente en tu orden. Estado de tu orden:Pendiente','success')
    return redirect(url_for('auth.index'))