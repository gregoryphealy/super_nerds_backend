# Create models (database tables) in this file
from .extensions import db


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    email = db.Column(db.String(128))
    password = db.Column(db.String(32))
    account_balance = db.Column(db.Float)

    # One to One Relationship
    banks = db.relationship('Banks', backref='users', uselist=False)


class Banks(db.Model):
    account_number = db.Column(db.Integer, primary_key=True,
                               autoincrement=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))


class Transactions(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True)
