from flask_login import (
    login_required,
    login_manager,
    UserMixin,
    login_user,
    logout_user,
    current_user,
)
from flask import Blueprint, render_template, flash, request, redirect, url_for
from sqlalchemy.exc import IntegrityError
from werkzeug.utils import secure_filename
import os
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text
from app import db, login_manager
from app.config import UPLOAD_FOLDER
from app.models.producto import Producto
from app.models.pedido import Pedido

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
            usuarioActual = current_user
            if usuarioActual.is_authenticated:
                cantidad_pedidos = Pedido.query.filter_by(usuarioForaneo=usuarioActual.idUsuario).count()
            else:
                cantidad_pedidos = 0
            return render_template('administrador/producto/add.html', cantidad_pedidos=cantidad_pedidos)
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
                    flash('Error al añadir producto', 'error')
                    return redirect(request.url)
            else:
                flash('Tipo de archivo no permitido', 'error')
                return redirect(request.url)
    else:
        flash('No tienes permiso para acceder a esta página', 'error')
        logout_user()
        return redirect(url_for('auth.index'))



@bp.route('/producto-edit/<int:idProducto>', methods=['GET', 'POST'])
@login_required
def edit(idProducto):
    if current_user.es_administrador==1:
        if request.method=='GET':
            producto=Producto.query.filter_by(idProducto=idProducto).first()
            usuarioActual = current_user
            if usuarioActual.is_authenticated:
                cantidad_pedidos = Pedido.query.filter_by(usuarioForaneo=usuarioActual.idUsuario).count()
            else:
                cantidad_pedidos = 0
            return render_template('administrador/producto/edit.html', producto=producto, cantidad_pedidos=cantidad_pedidos)
        elif request.method=='POST':
            idProducto = request.form['fIdProducto']
            productoSeleccionado = Producto.query.filter_by(idProducto=idProducto).first()
            nombreNuevo = request.form['fNombreProducto']
            precioNuevo = float(request.form['fPrecioProducto'])
            imagen = request.files['fImagen']

            if not nombreNuevo or not precioNuevo:
                flash('Ningún campo puede estar vacío', 'error')
                return redirect(request.url)
                
            # Verifica si el archivo cargado es válido
            imagen = request.files['fImagen']
            imagen_actual = request.form['fImagenActual']

            if imagen:
                # Se envió una nueva imagen, guarda la imagen como se hacía antes.
                filename = secure_filename(imagen.filename)
                imagen_guardada_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                imagen.save(imagen_guardada_path)
                productoSeleccionado.nombreProducto = nombreNuevo
                productoSeleccionado.precioProducto = precioNuevo
                productoSeleccionado.nombreImagen = filename
                
                try:
                    db.session.commit()
                    flash('Producto editado', 'success')
                    return redirect(url_for('auth.index'))
                except IntegrityError:
                    db.session.rollback()
                    flash('Error al Editar producto', 'error')
                    return redirect(request.url)
                
            elif not imagen:
                filename = imagen_actual
                    
                productoSeleccionado.nombreProducto = nombreNuevo
                productoSeleccionado.precioProducto = precioNuevo
                productoSeleccionado.nombreImagen = filename
                    
                try:
                    db.session.commit()
                    flash('Producto editado', 'success')
                    return redirect(url_for('auth.index'))
                except IntegrityError:
                    db.session.rollback()
                    flash('Error al Editar producto', 'error')
                    return redirect(request.url)
            else:
                flash('Tipo de archivo no permitido', 'error')
                return redirect(request.url)
    else:
        flash("No tienes permiso para ejecutar esta accion.", "error")
        return redirect(url_for('auth.index'))
    
@bp.route('/producto-delete/<int:idProducto>', methods=['GET', 'POST'])
@login_required
def delete(idProducto):
    if current_user.es_administrador == 1:
        productoSeleccionado = Producto.query.filter_by(idProducto=idProducto).first()
        
        # Verifica si el producto seleccionado y su imagen existen
        if productoSeleccionado:
            imagen_path = os.path.join('app/static/images/productos/', productoSeleccionado.nombreImagen)
            if os.path.exists(imagen_path):
                os.remove(imagen_path)
            else:
                flash('El archivo de imagen no existe', 'error')
                return redirect(url_for('auth.index'))
        else:
            flash('El producto seleccionado no existe', 'error')
        
        # Elimina el producto de la base de datos
        db.session.delete(productoSeleccionado)
        db.session.execute(text("ALTER TABLE producto AUTO_INCREMENT = 0"))
        db.session.commit()
            
        flash('Producto eliminado correctamente', 'success')
        return redirect(url_for('auth.index'))
    else:
        flash("No tienes permiso para ejecutar esta acción.", "error")
        return redirect(url_for('auth.index'))