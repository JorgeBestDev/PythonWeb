from app import db

class PaymentMethod(db.Model):
    __tablename__ = 'Payment_method'
    idPayment_method = db.Column(db.Integer, primary_key=True)
    nombrePaymentMethod = db.Column(db.String(255), nullable=False)
    imagen = db.Column(db.String(4096), nullable=False)
    usuario = db.relationship('Usuario', backref='payment_method', lazy='dynamic')
