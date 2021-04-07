from datetime import datetime
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# from flask import current_app
from finance_app import db#, login_manager
# from flask_login import UserMixin


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False) # "buy", "sell", "drop"
    date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    amount = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Transaction('ID: {self.id}', 'Type: {self.carries}', 'amount: {self.amount}', 'price: {self.price}')"
