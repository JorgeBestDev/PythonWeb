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
from app.models.producto import Producto


bp = Blueprint('producto', __name__)

@bp.route('/producto-add')
@login_required
def add():
    if current_user.es_administrador==1:
        if request.method=='GET':
            return render_template('administrador/producto/add.html')
        elif request.method =='POST':
            nombreProducto = request.form['fNombreProducto']
            precioProducto = request.form['fPrecioProducto']
            nombreImagen = request.form['fImagen']
            
            
            return 'exito al añadir producto'
    else:
        flash("No tienes permiso para acceder a esta página.", "error")
        logout_user()
        return redirect(url_for('auth.index'))


@bp.route('/producto-edit')
@login_required
def edit():
    if current_user.es_administrador:
        # Esta ruta solo es accesible para el administrador
        return render_template('ruta_exclusiva_admin.html')
    else:
        flash("No tienes permiso para ejecutar esta accion.", "error")
        return redirect(url_for('auth.index'))
    
@bp.route('/producto-delete')
@login_required
def delete():
    if isinstance(current_user, Administrador):
        # Esta ruta solo es accesible para el administrador
        return render_template('ruta_exclusiva_admin.html')
    else:
        flash("No tienes permiso para ejecutar esta accion.", "error")
        return redirect(url_for('auth.index'))