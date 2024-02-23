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
from sqlalchemy import text
from app.models.usuario import Usuario
from app.models.producto import Producto
from app.models.carrito import Carrito
from app.models.pedido import Pedido
from sqlalchemy.exc import IntegrityError

bp = Blueprint('carrito', __name__)

@bp.route('/carrito')
@login_required
def index():
    usuarioActual = current_user
    if usuarioActual.is_authenticated:
        cantidad_pedidos = Pedido.query.filter_by(usuarioForaneo=usuarioActual.idUsuario).count()
    else:
        cantidad_pedidos = 0
    
    pedidos_usuario = Pedido.query.filter_by(usuarioForaneo=usuarioActual.idUsuario).all()
    detalles_carritos = []
    
    for pedido in pedidos_usuario:
        carrito = Carrito.query.filter_by(pedidoForaneo=pedido.idPedido).first()
        if carrito:
            detalles_carrito = {
                'pedido': pedido,
                'productos': [],
            }

            # 4. Para cada carrito, obtén los productos y sus cantidades
            pedidos_en_carrito = Pedido.query.filter_by(idPedido=carrito.pedidoForaneo).all()
            for pedido_carrito in pedidos_en_carrito:
                producto = Producto.query.get(pedido_carrito.productoForaneo)
                detalles_producto = {
                    'nombre': producto.nombreProducto,
                    'cantidad': pedido_carrito.cantidadPedido,
                    'imagen': producto.nombreImagen,
                    'precio': pedido_carrito.totalPedido,
                }
                detalles_carrito['productos'].append(detalles_producto)

            detalles_carritos.append(detalles_carrito)
            


    return render_template('administrador/carrito/index.html', cantidad_pedidos=cantidad_pedidos, detalles_carritos=detalles_carritos)

@bp.route('/carrito/eliminar_pedido/<int:pedido_id>', methods=['POST'])
@login_required
def eliminar_pedido(pedido_id):
    pedido = Pedido.query.get_or_404(pedido_id)
    db.session.delete(pedido)
    db.session.commit()

    return redirect(url_for('carrito.index'))

@bp.route('/carrito/editar-producto/<int:pedido_id>', methods=['POST'])
@login_required
def editar_pedido(pedido_id):
    if request.method == 'POST':
        carrito = Carrito.query.filter_by(pedidoForaneo=pedido_id).first()

        if carrito:
            action = request.form.get('action')

            if action == 'minus':
                # Restar un producto al pedido
                if carrito.pedidoForaneo.cantidadPedido > 1:
                    carrito.pedidoForaneo.cantidadPedido -= 1
            elif action == 'plus':
                # Sumar un producto al pedido
                carrito.pedidoForaneo.cantidadPedido += 1

            # Guardar los cambios en la base de datos
            db.session.commit()
    
    return redirect(url_for('carrito.index'))