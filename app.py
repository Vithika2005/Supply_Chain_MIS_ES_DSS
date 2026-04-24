from flask import Flask
from config import Config
from database.db import db
from routes.iot import iot_bp
from routes.inventory import inventory_bp
from routes.analytics import analytics_bp
from routes.supplier import supplier_bp
from routes.report import report_bp
from routes.health import health_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(iot_bp)
app.register_blueprint(inventory_bp)
app.register_blueprint(analytics_bp)
app.register_blueprint(supplier_bp)
app.register_blueprint(report_bp)
app.register_blueprint(health_bp)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "Supply Chain MIS is running 🚀"

if __name__ == "__main__":
    app.run(debug=True)
