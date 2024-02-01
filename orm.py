from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Numeric, Enum,relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definir el modelo (una tabla en la base de datos)
Base = declarative_base()

class Categoria_has_producto(Base):
    __tablename__ = 'categoria_has_producto'
    categoriaForaneo = Column(Integer,  ForeignKey('categoria.idCategoria'), primary_key=True)
    productoForaneo = Column(Integer,  ForeignKey('producto.idProducto'), primary_key=True)
    
class Categoria(Base):
    __tablename__ = 'categoria'
    
    idCategoria = Column(Integer, primary_key=True)
    nombreCategoria = Column(String(255), nullable=False)
    
PENDING ='PENDING'
COMPLETED = 'COMPLETED'

class Orden(Base):
    __tablename__ = 'orden'
    
    idOrden = Column(Integer,  primary_key=True)
    usuarioForaneo = Column(Integer,  ForeignKey('usuario.idUsuario'), nullable=False)
    precioOrden = Column(Numeric(presicion=10, scale=2), nullable=False)
    status = Column(Enum(PENDING, COMPLETED, name='status_enum'), default=PENDING, nullable=False)
    pedido = relationship('Pedido', backref='orden', lazy='dynamic')
    
class PaymentMethod(Base):
    __tablename__ = 'payment_method'
    idPaymentMethod =  Column( Integer, primary_key=True)
    nombrePaymentMethod = Column( String(255), nullable=False)
    usuario = relationship('Usuario', backref='payment_method', lazy='dynamic')

class Pedido(Base):
    __tablename__ = 'pedido'
    
    idPedido = Column(Integer,  primary_key=True)
    ordenForaneo = Column(Integer,  ForeignKey('orden.idOrden'), nullable=False)
    productoForaneo = Column(Integer,  ForeignKey('producto.idProducto'), nullable=False)
    cantidadPedido = Column(Integer, nullable=False, default=1)
    totalPedido = Column(Numeric(presicion=10, scale=2), nullable=False)
    

class Producto(Base):
    __tablename__ = 'producto'
    idProducto = Column(Integer, primary_key=True)
    nombreProducto = Column(String(255), nullable=False, index=True)
    precioProducto = Column(Numeric(presicion=10, scale=2), nullable=False)
    pedido = relationship('Pedido', backref='producto', lazy='dynamic')
    
class Usuario(Base):
    __tablename__ = 'usuario'
    idUsuario = Column(Integer, primary_key=True)
    nommbreUsuario =Column(String(255), nullable=False)
    correoUsuario = Column(String(255), nullable=False)
    contraseñaUsuario = Column(String(255), nullable=False)
    payment_method_id = Column(Integer, ForeignKey('paymentMethod.idPaymentMethod'))
    orden = relationship('Orden', backref='usuario', lazy='dynamic')
    
# Modificar la URL de conexión para MySQL
# Sustituye 'usuario', 'contraseña', 'localhost' y 'nombre_de_base_de_datos' con tus propios valores
engine = create_engine('mysql+pymysql://root:BeDdh5AEHg23fGbEGca4-Dbb3ch6DC2e@viaduct.proxy.rlwy.net:15114/proyecto_formativo')

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión de SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

# Operaciones CRUD (igual que en el ejemplo anterior)

# Cerrar la sesión
session.close()