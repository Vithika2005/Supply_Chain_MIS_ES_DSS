from flask import Blueprint, jsonify
from services.simulation import generate_sensor_data
from services.rule_engine import check_alerts, classify_alert
from database.db import db
from database.models import SensorData, Alert

iot_bp = Blueprint("iot", __name__)

@iot_bp.route("/sensor", methods=["GET"])
def sensor():
    data = generate_sensor_data()

    # Save sensor data to DB
    sensor_entry = SensorData(**data)
    db.session.add(sensor_entry)

    # Existing rule-based alerts
    alerts = check_alerts(data)

    for a in alerts:
        db.session.add(Alert(message=a))

    # New severity classification (Expert System)
    severity = classify_alert(
        data["temperature"],
        data["humidity"],
        data["stock_level"]
    )

    db.session.commit()

    return jsonify({
        "data": data,
        "alerts": alerts,
        "severity": severity
    })
