from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import timedelta


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config['SECRET_KEY'] = 'claveSecreta'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=365)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'usuario.login'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'jorgito475@gmail.com'
    app.config['MAIL_PASSWORD'] = 'Jorgeivan123._.'

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        from .models.usuario import Usuario
        return Usuario.query.get(int(user_id))

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