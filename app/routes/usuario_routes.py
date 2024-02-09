from flask import Blueprint, render_template, session
from app import db
from app.models.usuario import Usuario


bp = Blueprint('usuario', __name__)

@bp.route('/usuario')
def index():
    Usuario = Usuario.query.all()
    return render_template('usuario/index.html', Usuario=Usuario)

@bp.route('/auth')
def register():
    return render_template('auth/register.html')


@bp.route('/dashboard')
def dashboard():
    is_session_active = 'username' in session
    return render_template('index.html', is_session_active=is_session_active)