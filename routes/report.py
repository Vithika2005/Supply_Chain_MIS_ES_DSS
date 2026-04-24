from flask import Blueprint
from reportlab.pdfgen import canvas

report_bp = Blueprint("report", __name__)

@report_bp.route("/report")
def generate_report():
    file_name = "supply_chain_report.pdf"

    c = canvas.Canvas(file_name)

    c.drawString(100, 800, "Supply Chain MIS Report")
    c.drawString(100, 770, "Generated Successfully")

    c.save()

    return f"{file_name} created successfully"
