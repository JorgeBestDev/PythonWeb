from flask_login import (
    login_required,
    login_manager,
    UserMixin,
    login_user,
    logout_user,
    current_user,
)
from flask import Blueprint, render_template, flash, request, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from app.models.usuario import Usuario
from app.models.administrador import Administrador
from app.models.pais import Pais
from app.models.producto import Producto
from sqlalchemy.exc import IntegrityError



bp = Blueprint("auth", __name__)



@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        first_name = request.form["first-name"]
        last_name = request.form["last-name"]
        correoUsuario = request.form["fCorreoUsuario"]
        contraseñaUsuario = request.form["fContraseña"]
        telefonoUsuario = request.form["fTelefonoUsuario"]
        pais = request.form["fPais"]
        direccion = request.form["fDireccion"]
        ciudad = request.form["fCiudad"]
        estado = request.form["fEstado"]
        codigoPostal = request.form["fCodigoPostal"]

        if not all(
            [
                first_name,
                last_name,
                correoUsuario,
                contraseñaUsuario,
                telefonoUsuario,
                pais,
                direccion,
                ciudad,
                estado,
                codigoPostal,
            ]
        ):
            flash("Por favor, completa todos los campos del formulario.", "error")
            return redirect(request.url)

        nombreUsuario = f"{first_name} {last_name}"  # Concatenar nombre de usuario

        contraseña_encriptada = generate_password_hash(contraseñaUsuario)

        user = Usuario(
            nombreUsuario=nombreUsuario,
            correoUsuario=correoUsuario,
            contraseñaUsuario=contraseña_encriptada,
            telefonoUsuario=telefonoUsuario,
            pais_id=pais,
            direccion=direccion,
            estado=estado,
            ciudad=ciudad,
            codigoPostal=codigoPostal,
        )

        try:
            db.session.add(user)
            db.session.commit()
            flash("Usuario registrado", "success")
            return render_template("auth/login.html")
        except IntegrityError:
            db.session.rollback()
            flash("Correo ya existente", "error")
            return redirect(request.url)
    paises = Pais.query.all()
    return render_template("auth/register.html", paises=paises)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        
        correo = request.form["fCorreoUsuario"]
        contraseña = request.form["fContraseñaUsuario"]
        admin = Administrador.query.filter_by(correoAdministrador=correo).first()
        user = Usuario.query.filter_by(correoUsuario=correo).first()
        if not user and not admin:  
            flash('No hay ningun correo asociado a tu cuenta.', 'error')
            return redirect(request.url)
        if admin:
            
            if check_password_hash(admin.contraseñaAdministrador, contraseña):
                login_user(admin)
                
                
                if isinstance(current_user, Administrador):
                    # Esta ruta solo es accesible para el administrador
                    return redirect(url_for('administrador.index'))
                else:
                    flash("No tienes permiso para acceder a esta página.", "error")
                    return redirect(url_for("auth.index"))
            else:
                flash("Contraseña incorrecta", "error")
                return redirect(request.url)
        else:
            if user:
                if check_password_hash(user.contraseñaUsuario, contraseña):
                    login_user(user)
                    return redirect(url_for("auth.index"))
                else:
                    flash("Contraseña incorrecta", "error")
                    return redirect(request.url)
                    
            else:
                flash("Usuario incorrecto", "error")
            return redirect(request.url)
    return render_template("auth/login.html")


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.index"))


@bp.route("/")
def index():
    productos = Producto.query.all()
    usuarioActual = current_user
    return render_template("index.html", current_user=usuarioActual, productos=productos)