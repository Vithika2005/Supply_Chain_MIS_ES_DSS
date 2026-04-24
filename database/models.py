from database.db import db
from datetime import datetime

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
    reorder_level = db.Column(db.Integer)

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    stock_level = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String(100))
    delivery_delay = db.Column(db.Integer)
    quality_score = db.Column(db.Float)
    cost_score = db.Column(db.Float)
    reliability_score = db.Column(db.Float)
