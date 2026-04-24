from flask import Blueprint, jsonify
from database.models import Inventory
from services.health_score import calculate_health_score

health_bp = Blueprint("health", __name__)

@health_bp.route("/health")
def warehouse_health():
    # sample simulated values
    temperature = 38
    humidity = 78

    inventory = Inventory.query.all()

    low_stock_count = sum(
        1 for item in inventory
        if item.quantity < item.reorder_level
    )

    critical_alerts = 2

    score = calculate_health_score(
        temperature,
        humidity,
        low_stock_count,
        critical_alerts
    )

    return jsonify({
        "temperature": temperature,
        "humidity": humidity,
        "low_stock_count": low_stock_count,
        "critical_alerts": critical_alerts,
        "warehouse_health_score": score
    })
