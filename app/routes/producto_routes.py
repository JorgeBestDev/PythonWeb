from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import (
    login_required,
    login_manager,
    UserMixin,
    login_user,
    logout_user,
    current_user,
)
from werkzeug.utils import secure_filename
import os
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash
from app import db, login_manager
from app.config import UPLOAD_FOLDER
from app.models.producto import Producto

from flask import current_app as app

bp = Blueprint('producto', __name__)


carpeta = 'static'
subcarpeta = 'images'
productos = 'productos'
ruta_archivo = os.path.join(carpeta, subcarpeta, productos)

# Asegúrate de que la ruta de la carpeta exista
if not os.path.exists(ruta_archivo):
    os.makedirs(ruta_archivo)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}



@bp.route('/producto-add', methods=['GET', 'POST'])
@login_required
def add():
    from app import create_app
    app=create_app()
    if current_user.es_administrador:
        if request.method == 'GET':
            return render_template('administrador/producto/add.html')
        elif request.method == 'POST':
            nombreProducto = request.form['fNombreProducto']
            precioProducto = request.form['fPrecioProducto']
            imagen = request.files['fImagen']
            
            if not nombreProducto or not precioProducto or not imagen:
                flash('Ningún campo puede estar vacío', 'error')
                return redirect(request.url)
            
            # Verifica si el archivo cargado es válido
            if imagen:
                # Genera un nombre seguro para el archivo
                filename = secure_filename(imagen.filename)
                imagen_guardada_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                imagen.save(imagen_guardada_path)
                
                producto = Producto(
                    nombreProducto=nombreProducto,
                    precioProducto=precioProducto,
                    nombreImagen=filename  # Guarda el nombre del archivo en la base de datos
                )
                
                try:
                    db.session.add(producto)
                    db.session.commit()
                    flash('Producto registrado', 'success')
                    return redirect(url_for('auth.index'))
                except IntegrityError:
                    db.session.rollback()
                    flash('Correo ya existente', 'error')
                    return redirect(request.url)
            else:
                flash('Tipo de archivo no permitido', 'error')
                return redirect(request.url)
    else:
        flash('No tienes permiso para acceder a esta página', 'error')
        logout_user()
        return redirect(url_for('auth.index'))



@bp.route('/producto-edit')
@login_required
def edit():
    if current_user.es_administrador==1:
        if request.method=='GET':
            producto = Producto.query.all()
            return render_template('ruta_exclusiva_admin.html', producto)
        elif request.method=='POST':

            return 'Edito producto'
    else:
        flash("No tienes permiso para ejecutar esta accion.", "error")
        return redirect(url_for('auth.index'))
    
@bp.route('/producto-delete')
@login_required
def delete():
    if current_user.es_administrador:
        # Esta ruta solo es accesible para el administrador
        return render_template('ruta_exclusiva_admin.html')
    else:
        flash("No tienes permiso para ejecutar esta accion.", "error")
        return redirect(url_for('auth.index'))