from flask import Blueprint, jsonify
from database.models import Inventory
from services.reorder_engine import reorder_recommendation

inventory_bp = Blueprint("inventory", __name__)

@inventory_bp.route("/inventory", methods=["GET"])
def get_inventory():
    items = Inventory.query.all()

    result = []

    for item in items:
        forecast = 100  # simple fixed forecast for now

        recommended_reorder = reorder_recommendation(
            item.quantity,
            forecast
        )

        result.append({
            "product": item.product_name,
            "quantity": item.quantity,
            "reorder_level": item.reorder_level,
            "recommended_reorder": recommended_reorder
        })

    return jsonify(result)
