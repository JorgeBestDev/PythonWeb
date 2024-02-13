from flask import Blueprint, render_template, session, flash, request, redirect, url_for
#from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models.usuario import Usuario


bp = Blueprint('usuario', __name__)

@bp.route('/usuario')
def index():
    Usuario = Usuario.query.all()
    return render_template('usuario/index.html', Usuario=Usuario)

@bp.route('/register')
def register():
    return render_template('auth/register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')
#    if request.method == 'POST':
#        username = request.form['fUsuario']
#        password = request.form['fContraseña']
        
#        return render_template('auth/login.html')
#    else:
#        return render_template('auth/login.html')

    

        


@bp.route('/dashboard')
def dashboard():
    is_session_active = 'username' in session
    return render_template('index.html', is_session_active=is_session_active)