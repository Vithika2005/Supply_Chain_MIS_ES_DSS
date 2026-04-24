def calculate_health_score(temp, humidity, low_stock_count, critical_alerts):
    score = 100

    if temp > 35:
        score -= 15

    if humidity > 75:
        score -= 10

    score -= (low_stock_count * 5)
    score -= (critical_alerts * 10)

    if score < 0:
        score = 0

    return score
