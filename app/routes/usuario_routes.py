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
    return redirect(url_for("auth.login"))


@bp.route("/dashboard/edit", methods=["GET", "POST"])
@login_required
def edit():
    if current_user.is_authenticated:
        if request.method == "GET":
            usuario = current_user
            paises = Pais.query.all()
            paisActual = usuario.country_obj
            return render_template(
                "usuario/edit.html",
                usuario=usuario,
                paises=paises,
                paisActual=paisActual,
            )
        if request.method == "POST":
            nombreUsuario = request.form["fNombreUsuario"]
            correoUsuario = request.form["fCorreoUsuario"]
            telefonoUsuario = request.form["fTelefonoUsuario"]
            pais = request.form["fPais"]
            direccion = request.form["fDireccion"]
            estado = request.form["fEstado"]
            ciudad = request.form["fCiudad"]
            codigoPostal = request.form["fCodigoPostal"]

            current_user.nombreUsuario = nombreUsuario
            current_user.correoUsuario = correoUsuario

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


@bp.route("/changePassword", methods=["GET", "POST"])
@login_required
def change_password():
    print("usuario actual", current_user)
    if request.method == "GET":
        return render_template("usuario/change_password.html")

    if request.method == "POST":
        old_password = request.form["fPasswordAntigua"]
        new_password = request.form["fPasswordNueva"]
        confirmation = request.form["fConfirmacion"]
        if not old_password or not new_password or not confirmation:
            flash("Ningun campo puede estar vacío", "warning")
            return redirect(url_for("usuario.change_password"))
        else:
            if not current_user.check_password(old_password):
                flash("La contraseña actual es incorrecta.", "error")
                return redirect(url_for("usuario.change_password"))
            elif new_password != confirmation:
                flash("La nueva contraseña no coincide con la confirmación", "error")
                return redirect(url_for("usuario.change_password"))
            else:
                contraseña_encriptada = generate_password_hash(new_password)
                current_user.contraseñaUsuario = contraseña_encriptada
                db.session.commit()
                flash("Se ha cambiado su contraseña exitosamente", "success")
                return redirect(url_for("usuario.edit"))


@bp.route("/dashboard")
@login_required
def dashboard():
    usuario = current_user
    paises = Pais.query.all()
    paisActual = usuario.country_obj
    return render_template(
        "usuario/edit.html", usuario=usuario, paises=paises, paisActual=paisActual
    )
