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
    carrito = Carrito.query.all()
    usuarioActual = current_user
    if usuarioActual.is_authenticated:
        cantidad_pedidos = Pedido.query.filter_by(usuarioForaneo=usuarioActual.idUsuario).count()
    else:
        cantidad_pedidos = 0
    pedido = Pedido.query.filter_by(usuarioForaneo=usuarioActual.idUsuario)
    usuarioActualId=usuarioActual.idUsuario
    consulta = db.session.execute(text("select pedido.idPedido from pedido where pedido.usuarioForaneo=:usuarioActual"), {"usuarioActual": usuarioActualId})
    producto = db.session.execute(text("select producto.idProducto from producto where pedido.productoForaneo=:"))
    resultados = consulta.fetchall()

    db.session.close()

    
    return render_template('administrador/carrito/index.html', Carrito=carrito, cantidad_pedidos=cantidad_pedidos, resultados=carrito)