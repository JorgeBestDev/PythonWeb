from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app import db
from app.models.payment_Method import PaymentMethod


bp = Blueprint('payment_method', __name__)

@bp.route('/Payment_methods')
def index():
    PaymentMethod = PaymentMethod.query.all()
    return render_template('usuario/payment_methods/index.html', PaymentMethod=PaymentMethod)