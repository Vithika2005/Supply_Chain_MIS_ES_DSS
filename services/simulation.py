import random
import time

def generate_sensor_data():
    return {
        "temperature": random.uniform(15, 40),
        "humidity": random.uniform(30, 90),
        "stock_level": random.randint(0, 500)
    }
