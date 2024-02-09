from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app import db
from app.models.usuario import Usuario


bp = Blueprint('usuario', __name__)

@bp.route('/usuario')
def index():
    Usuario = Usuario.query.all()
    return render_template('usuario/index.html', Usuario=Usuario)

@bp.route('/auth')
def registerLogin():
    return render_template('auth/register-login.html')