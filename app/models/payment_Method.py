from app import db

class PaymentMethod(db.Model):
    __tablename__ = 'Payment_methods'
    idPayment_methods = db.Column(db.Integer, primary_key=True)
    nombrePaymentMethod = db.Column(db.String(255), nullable=False)
    usuarios = db.relationship('Usuario', backref='payment_method', lazy='dynamic')
