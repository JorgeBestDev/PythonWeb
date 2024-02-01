from flask import Blueprint

bp = Blueprint('main', __name__)

from app.routes import categoria_has_product_routes, categoria_routes, orden_routes, payment_method_routes, pedido_routes, producto_routes, usuario_routes
