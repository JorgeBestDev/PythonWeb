from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    init_extensions(app)
    register_blueprints(app)

    return app

def init_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'


    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        from .models.usuario import Usuario
        return Usuario.query.get(int(user_id))
    
def register_blueprints(app):
    from app.routes import (categoria_has_product_routes, categoria_routes,
                            orden_routes, payment_method_routes,
                            pedido_routes, producto_routes,
                            usuario_routes, pais_routes,
                            auth_routes, administrador_routes,
                            usuario_has_orden_routes)
    app.register_blueprint(categoria_has_product_routes.bp)
    app.register_blueprint(categoria_routes.bp)
    app.register_blueprint(orden_routes.bp)
    app.register_blueprint(payment_method_routes.bp)
    app.register_blueprint(pedido_routes.bp)
    app.register_blueprint(producto_routes.bp)
    app.register_blueprint(usuario_routes.bp)
    app.register_blueprint(pais_routes.bp)
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(administrador_routes.bp)
    app.register_blueprint(usuario_has_orden_routes.bp)