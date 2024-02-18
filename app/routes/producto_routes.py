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
from app.models.administrador import Administrador
from app.models.producto import Producto


bp = Blueprint('producto', __name__)

@bp.route('/ruta-exclusiva-admin')
@login_required
def ruta_exclusiva_admin():
    if isinstance(current_user, Administrador):
        # Esta ruta solo es accesible para el administrador
        return render_template('ruta_exclusiva_admin.html')
    else:
        flash("No tienes permiso para acceder a esta página.", "error")
        return redirect(url_for('auth.index'))


@bp.route('/añadirProducto')
def add():
    return render_template('producto/add.html', Producto=Producto)

@bp.route('/editarProducto')
def edit():
    return render_template('producto/add.html', Producto=Producto)

@bp.route('/eliminarProducto')
def delete():
    return 'Eliminar'