from flask import Blueprint, render_template, session, flash, request, redirect, url_for
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash,generate_password_hash
from app import db
from app.models.usuario import Usuario
from app.models.pais import Pais


bp = Blueprint('usuario', __name__)

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
            return 'Username or email already exists!'
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
                session['username'] = user.nombreUsuario
                session.permanent = True
                return redirect(url_for('usuario.dashboard'))
            else:
                flash(user.contraseñaUsuario, 'error')
        else:
            flash('Usuario incorrecto', 'error')
    return render_template('auth/login.html')


@bp.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('index.html')


@bp.route('/dashboard')
def dashboard():
    is_session_active = 'username' in session
    username = session.get('username')
    return render_template('index.html', is_session_active=is_session_active, username=username)


@bp.route('/usuario')
def index():
    username = session.get('username')
    if username:
        is_session_active = 'username' in session
        return render_template('usuario/index.html', is_session_active=is_session_active, username=username)
    return render_template("auth/login.html")
    




