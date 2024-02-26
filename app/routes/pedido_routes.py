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
from sqlalchemy import text
from app import db
from app.models.producto import Producto
from app.models.pedido import Pedido
from app.models.carrito import Carrito

from flask import current_app as app


bp = Blueprint('pedido', __name__)

@bp.route('/pedido')
def index():
    Pedido = Pedido.query.all()
    return render_template('pedido/index.html', Pedido=Pedido)

@bp.route('/add-to-cart/<int:idProducto>', methods=['GET','POST'])
@login_required
def add_to_cart(idProducto):
    if request.method=='POST':
        try:
            producto = Producto.query.get_or_404(idProducto)
            cantidad = int(request.form['fCantidad'])
            totalPedido = producto.precioProducto * cantidad
            
            # Verifica si el producto ya está en el carrito
            pedido_existente = Pedido.query.filter_by(productoForaneo=idProducto, usuarioForaneo=current_user.idUsuario).first()
            if pedido_existente:
                # Actualiza la cantidad del producto existente en el carrito
                pedido_existente.cantidadPedido += cantidad
                pedido_existente.totalPedido += totalPedido
            else:
                # Crea un nuevo pedido
                pedido = Pedido(
                    productoForaneo=idProducto,
                    usuarioForaneo=current_user.idUsuario,
                    cantidadPedido=cantidad,
                    totalPedido=totalPedido
                )
                db.session.add(pedido)
            
            db.session.commit()
            
            # Verifica si se agregó un nuevo pedido o se actualizó la cantidad del producto existente
            if not pedido_existente:
                # Crea un nuevo carrito si se agregó un nuevo pedido
                carrito = Carrito(
                    pedidoForaneo=pedido.idPedido
                )
                db.session.add(carrito)
                db.session.commit()
            
            flash("Se ha agregado el producto al carrito de compras", 'success')
            return redirect(url_for('auth.index'))
        except (AttributeError, ValueError):
            flash("No fue posible realizar la operación, inténtelo nuevamente.", 'error')
            return redirect(url_for('auth.index'))