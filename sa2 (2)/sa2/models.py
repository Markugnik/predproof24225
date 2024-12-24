from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    login = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    
class UserSession(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    login = db.Column(db.String(25), nullable=False)
    order_id = db.Column(db.Integer, nullable=False)

class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=True, default=0)
    sup_id = db.Column(db.Integer, nullable=False)
    desc_id = db.Column(db.Integer, nullable=False)
    gds_avail = db.Column(db.Integer, nullable=True, default=0)
    gds_ordered = db.Column(db.Integer, nullable=True, default=0) # е
    gds_state = db.Column(db.String(20), default='scrap')
    gds_name = db.Column(db.String(30), nullable=True)
    
class GoodDesc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gds_desc = db.Column(db.String(240), nullable=True)
    gds_url = db.Column(db.String(30), nullable=True)
    gds_desc = db.Column(db.String(240), nullable=True)

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=True, default=0)
    ord_type = db.Column(db.Integer, nullable=True, default=0)
    ord_status = db.Column(db.Integer, nullable=True, default=0)
    ord_name = db.Column(db.String(40), nullable=True)
    ord_desc = db.Column(db.String(240), nullable=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=True)
    
class Suppliers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supname = db.Column(db.String(25), unique=True, nullable=False)
    suptel = db.Column(db.String(15), nullable=True)
    supemail = db.Column(db.String(50), nullable=True)
    supurl = db.Column(db.String(150), nullable=True)
