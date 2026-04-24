def check_alerts(sensor):
    alerts = []

    if sensor["temperature"] > 35:
        alerts.append("High Temperature Alert")

    if sensor["stock_level"] < 50:
        alerts.append("Low Stock Alert")

    return alerts
def classify_alert(temp, humidity, stock):
    if temp > 40:
        return "Critical"

    elif stock < 20:
        return "High"

    elif humidity > 75:
        return "Medium"

    else:
        return "Low"
