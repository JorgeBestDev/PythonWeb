from flask import Blueprint, render_template, session, flash, request, redirect, url_for
from flask_login import login_required, login_manager, UserMixin,login_user, logout_user,current_user
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash,generate_password_hash
from app import db, login_manager
from app.models.usuario import Usuario
from app.models.pais import Pais


bp = Blueprint('usuario', __name__)

@login_manager.unauthorized_handler
def unauthorized_callback():
    flash('Por favor inicia sesión para acceder a esta página.', 'error')
    return redirect(url_for('usuario.login'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        correoUsuario = request.form['fCorreoUsuario']
        contraseñaUsuario = request.form['fContraseña']
        pais = request.form['fPais']
        direccion = request.form['fDireccion']
        ciudad = request.form['fCiudad']
        estado = request.form['fEstado']
        codigoPostal = request.form['fCodigoPostal']
        
        if not all([first_name, last_name, correoUsuario, contraseñaUsuario, pais, direccion, ciudad, estado, codigoPostal]):
            flash('Por favor, completa todos los campos del formulario.', 'error')
            return redirect(request.url)

        nombreUsuario = f"{first_name} {last_name}"  # Concatenar nombre de usuario
        
        contraseña_encriptada = generate_password_hash(contraseñaUsuario)
        

        user = Usuario(nombreUsuario=nombreUsuario, correoUsuario=correoUsuario, contraseñaUsuario=contraseña_encriptada, pais_id=pais,
                    direccion=direccion, estado=estado, ciudad=ciudad, codigoPostal=codigoPostal)
        
        try:
            db.session.add(user)
            db.session.commit()
            flash('Usuario registrado', 'success')
            return render_template('auth/login.html')
        except IntegrityError:
            db.session.rollback()
            flash('Correo ya existente', 'error')
            return redirect(request.url)
    paises = Pais.query.all()
    return render_template('auth/register.html', paises=paises)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['fCorreoUsuario']
        contraseña = request.form['fContraseñaUsuario']
        user = Usuario.query.filter_by(correoUsuario=correo).first()
        if user:
            if check_password_hash(user.contraseñaUsuario, contraseña):
                login_user(user)
                return redirect(url_for('usuario.index'))
            else:
                flash('Contraseña incorrecta', 'error')
        else:
            flash('Usuario incorrecto', 'error')
    return render_template('auth/login.html')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('index.html')


@bp.route('/')
def index():
    usuario=current_user
    return render_template('index.html',usuario=usuario)


@bp.route('/dashboard')
@login_required
def dashboard():
    usuario=current_user
    return render_template('usuario/index.html', usuario=usuario)
    




