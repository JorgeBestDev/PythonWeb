from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import (
    login_required,
    login_manager,
    UserMixin,
    login_user,
    logout_user,
    current_user,
)
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash
from app import db, login_manager
from app.models.usuario import Usuario
from app.models.pais import Pais


bp = Blueprint("usuario", __name__)


@login_manager.unauthorized_handler
def unauthorized_callback():
    flash("Por favor inicia sesión para acceder a esta página.", "error")
    return redirect(url_for("usuario.login"))


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
        user = Usuario.query.filter_by(correoUsuario=correo).first()
        if user:
            if check_password_hash(user.contraseñaUsuario, contraseña):
                login_user(user)
                return redirect(url_for("usuario.index"))
            else:
                flash("Contraseña incorrecta", "error")
        else:
            flash("Usuario incorrecto", "error")
    return render_template("auth/login.html")


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("usuario.index"))


@bp.route("/")
def index():
    usuario = current_user
    return render_template("index.html", usuario=usuario)


@bp.route("/dashboard/edit", methods=["GET", "POST"])
@login_required
def edit():
    if current_user.is_authenticated:
        if request.method == "GET":
            usuario = current_user
            return render_template("usuario/edit.html", usuario=usuario)
        if request.method == "POST":
            nombreUsuario = request.form["fNombreUsuario"]
            correoUsuario = request.form["fCorreoUsuario"]
            contraseñaUsuario = request.form["fContraseñaUsuario"]
            telefonoUsuario = request.form["fTelefonoUsuario"]
            pais = request.form["fPais"]
            direccion = request.form["fDireccion"]
            estado = request.form["fEstado"]
            ciudad = request.form["fCiudad"]
            codigoPostal = request.form["fCodigoPostal"]

            current_user.nombreUsuario = nombreUsuario
            current_user.correoUsuario = correoUsuario

            contraseña_encriptada = generate_password_hash(contraseñaUsuario)
            current_user.contraseñaUsuario = contraseña_encriptada

            current_user.telefonoUsuario = telefonoUsuario
            current_user.pais = pais
            current_user.direccion = direccion
            current_user.estado = estado
            current_user.ciudad = ciudad
            current_user.codigoPostal = codigoPostal
            try:
                db.session.commit()
                return redirect(url_for("usuario.dashboard"))
            except IntegrityError:
                db.session.rollback()
            flash("No se puede editar usuario", "error")
            return redirect(request.url)

        usuario = current_user
        flash("No se edito el usuario")
        return render_template("index.html", usuario=usuario)
    return redirect(url_for("usuario.login"))


@bp.route("/dashboard/delete", methods=["GET", "POST"])
@login_required
def delete():
    if request.method == "POST":
        if current_user.is_authenticated:
            user_id = current_user.get_id()
            usuario = Usuario.query.get(user_id)
            if usuario:
                try:
                    db.session.delete(usuario)
                    db.engine.execute("ALTER TABLE usuario AUTO_INCREMENT=0")
                    db.session.commit()
                    flash("¡Usuario eliminado correctamente!", "success")
                    return redirect(url_for("usuario.index"))
                except Exception as e:
                    flash(f"Error al eliminar el usuario: {str(e)}", "error")
                return redirect(url_for("usuario.delete"))
        return redirect(url_for("usuario.login"))
    usuario = current_user
    return render_template("usuario/delete.html", usuario=usuario)


@bp.route("/restore_password")
def restore_password():
    return render_template("auth/restore_password.html")


@bp.route("/dashboard")
@login_required
def dashboard():
    usuario = current_user
    return render_template("usuario/edit.html", usuario=usuario)
