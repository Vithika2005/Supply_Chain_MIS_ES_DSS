from flask import Blueprint, jsonify
from database.models import Supplier
from services.supplier_score import calculate_supplier_score

supplier_bp = Blueprint("supplier", __name__)

@supplier_bp.route("/supplier")
def supplier_dashboard():
    suppliers = Supplier.query.all()

    result = []

    for s in suppliers:
        result.append({
            "supplier_name": s.supplier_name,
            "score": calculate_supplier_score(s)
        })

    return jsonify(result)
