from ..utils import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer(), primary_key=True)
    client = db.Column(db.String(20), nullable=False)
    order_title = db.Column(db.String(60))
    description = db.Column(db.Text())
    price = db.Column(db.Numeric(10, 2), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    due_date = db.Column(db.Date)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), primary_key=True)

    def __repr__(self):
        return f"Order {self.order_title}"
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()