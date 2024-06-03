from ..utils import db
from datetime import datetime


class Recipe(db.Model):
    __tablename__ = 'recipes'
    recipe_id = db.Column(db.Integer(), primary_key=True)
    pastry_name = db.Column(db.String(), nullable=False)
    ingredients = db.Column(db.String(), nullable=False)
    recipe = db.Column(db.Text())
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), primary_key=True)

    def __rep__(self):
        return f"Recipe for {self.pastry_name}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()