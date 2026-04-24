import pandas as pd
from app import app
from database.models import SensorData, Inventory, Alert

with app.app_context():
    inventory_data = [(i.product_name, i.quantity) for i in Inventory.query.all()]
    sensor_data = [(s.temperature, s.humidity, s.timestamp) for s in SensorData.query.all()]
    alert_data = [(a.message, a.timestamp) for a in Alert.query.all()]

    pd.DataFrame(inventory_data, columns=["product", "quantity"]).to_csv("inventory.csv", index=False)
    pd.DataFrame(sensor_data, columns=["temperature", "humidity", "timestamp"]).to_csv("sensor.csv", index=False)
    pd.DataFrame(alert_data, columns=["message", "timestamp"]).to_csv("alerts.csv", index=False)
