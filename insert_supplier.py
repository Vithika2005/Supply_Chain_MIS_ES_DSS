from app import app
from database.db import db
from database.models import Supplier

with app.app_context():
    db.session.add(Supplier(
        supplier_name="ABC Suppliers",
        delivery_delay=2,
        quality_score=9,
        cost_score=8,
        reliability_score=9
    ))

    db.session.add(Supplier(
        supplier_name="XYZ Traders",
        delivery_delay=5,
        quality_score=7,
        cost_score=6,
        reliability_score=7
    ))

    db.session.commit()

print("Supplier data inserted successfully!")
