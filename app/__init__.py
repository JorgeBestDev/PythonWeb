from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)

    from app.routes import categoria_has_product_routes, categoria_routes,orden_routes,payment_method_routes,pedido_routes,producto_routes,usuario_routes, pais_routes
    app.register_blueprint(categoria_has_product_routes.bp)
    app.register_blueprint(categoria_routes.bp)
    app.register_blueprint(orden_routes.bp)
    app.register_blueprint(payment_method_routes.bp)
    app.register_blueprint(pedido_routes.bp)
    app.register_blueprint(producto_routes.bp)
    app.register_blueprint(usuario_routes.bp)
    app.register_blueprint(pais_routes.bp)

    return app