from ..utils import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    orders = db.relationship('Order', backref='user', lazy=True)
    recipes = db.relationship('Recipe', backref='user', lazy=True)

    def __repr__(self):
        return f"User {self.username}"
    
    def save(self):
        db.session.add(self)
        db.session.commit()