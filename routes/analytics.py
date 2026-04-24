from flask import Blueprint, jsonify
from services.forecasting import forecast

analytics_bp = Blueprint("analytics", __name__)

@analytics_bp.route("/forecast", methods=["GET"])
def get_forecast():
    result = forecast()
    return jsonify({"forecast": result})
