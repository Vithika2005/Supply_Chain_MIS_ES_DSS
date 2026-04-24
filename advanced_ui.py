import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium
import requests

st.set_page_config(
    page_title="Supply Chain MIS",
    layout="wide"
)

st.title("📦 Intelligent IoT-Enabled Supply Chain MIS")
st.markdown("### MIS + DSS + ES + IoT + Analytics Dashboard")

# ---------------- SIDEBAR ----------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Dashboard",
        "Inventory",
        "Sensors",
        "Alerts",
        "Supplier Dashboard",
        "Forecast",
        "Reports"
    ]
)

# ---------------- API FETCH FUNCTION ----------------

def get_data(endpoint):
    try:
        response = requests.get(f"http://127.0.0.1:5000/{endpoint}")
        return response.json()
    except:
        return {}

# ---------------- DASHBOARD ----------------

if page == "Dashboard":
    st.header("📊 Executive Overview Dashboard")

    sensor = get_data("sensor")
    inventory = get_data("inventory")
    supplier = get_data("supplier")

    col1, col2, col3, col4 = st.columns(4)

    try:
        temp = sensor["data"]["temperature"]
        humidity = sensor["data"]["humidity"]
        stock = sensor["data"]["stock_level"]
        severity = sensor.get("severity", "Low")
    except:
        temp = 0
        humidity = 0
        stock = 0
        severity = "N/A"

    col1.metric("🌡 Temperature", f"{temp:.2f} °C")
    col2.metric("💧 Humidity", f"{humidity:.2f} %")
    col3.metric("📦 Stock Level", stock)
    col4.metric("🚨 Alert Severity", severity)

    st.divider()

    st.subheader("Quick Business Summary")

    if isinstance(inventory, list):
        st.write(f"Total Inventory Items: {len(inventory)}")

    if isinstance(supplier, list):
        st.write(f"Total Suppliers: {len(supplier)}")

# ---------------- INVENTORY ----------------

elif page == "Inventory":
    st.header("📦 Inventory Management + Reorder Engine")

    inventory = get_data("inventory")
    df = pd.DataFrame(inventory)

    if not df.empty:
        st.dataframe(df, use_container_width=True)

        fig = px.bar(
            df,
            x="product",
            y="quantity",
            title="Current Inventory Stock Levels"
        )
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("🧠 Smart Reorder Recommendation")

        if "recommended_reorder" in df.columns:
            reorder_df = df[
                ["product", "quantity", "reorder_level", "recommended_reorder"]
            ]
            st.dataframe(reorder_df, use_container_width=True)

        low_stock = df[df["quantity"] < 30]

        st.subheader("⚠ Low Stock Items")

        if not low_stock.empty:
            st.dataframe(low_stock, use_container_width=True)
        else:
            st.success("All inventory levels are healthy")

    else:
        st.warning("No inventory data available")

# ---------------- SENSORS ----------------

elif page == "Sensors":
    st.header("🌡 IoT Sensor Monitoring")

    sensor = get_data("sensor")

    if sensor:
        st.json(sensor)

        try:
            temp = sensor["data"]["temperature"]
            humidity = sensor["data"]["humidity"]

            sensor_df = pd.DataFrame({
                "Metric": ["Temperature", "Humidity"],
                "Value": [temp, humidity]
            })

            fig = px.bar(
                sensor_df,
                x="Metric",
                y="Value",
                title="Live Sensor Metrics"
            )

            st.plotly_chart(fig, use_container_width=True)

        except:
            st.warning("Sensor data format issue")

    else:
        st.warning("Sensor API not responding")

# ---------------- ALERTS ----------------

elif page == "Alerts":
    st.header("🚨 Expert System Alert Center")

    sensor = get_data("sensor")
    alerts = sensor.get("alerts", [])
    severity = sensor.get("severity", "Low")

    st.metric("Severity Level", severity)

    st.subheader("Generated Alerts")

    if alerts:
        for alert in alerts:
            st.error(alert)
    else:
        st.success("No alerts generated")

# ---------------- SUPPLIER DASHBOARD ----------------

elif page == "Supplier Dashboard":
    st.header("🏭 Supplier Performance Dashboard")

    supplier = get_data("supplier")
    df = pd.DataFrame(supplier)

    if not df.empty:
        st.dataframe(df, use_container_width=True)

        fig = px.bar(
            df,
            x="supplier_name",
            y="score",
            title="Supplier Performance Scores"
        )

        st.plotly_chart(fig, use_container_width=True)

        best_supplier = df.sort_values(
            by="score",
            ascending=False
        ).iloc[0]

        st.success(
            f"Best Supplier: {best_supplier['supplier_name']} "
            f"(Score: {best_supplier['score']})"
        )

    else:
        st.warning("No supplier data found")

# ---------------- FORECAST ----------------

elif page == "Forecast":
    st.header("📈 Demand Forecasting Dashboard")

    forecast = get_data("forecast")

    if forecast:
        st.json(forecast)

        try:
            forecast_df = pd.DataFrame({
                "Type": ["Actual", "Predicted"],
                "Value": [
                    forecast.get("actual", 100),
                    forecast.get("predicted", 120)
                ]
            })

            fig = px.line(
                forecast_df,
                x="Type",
                y="Value",
                markers=True,
                title="Actual vs Predicted Demand"
            )

            st.plotly_chart(fig, use_container_width=True)

        except:
            st.warning("Forecast data issue")

    else:
        st.warning("Forecast API unavailable")

# ---------------- REPORTS ----------------

elif page == "Reports":
    st.header("📄 PDF Report Generation")

    st.write("Generate management-ready MIS reports")

    if st.button("Generate PDF Report"):
        try:
            response = requests.get("http://127.0.0.1:5000/report")

            if response.status_code == 200:
                st.success("PDF Report generated successfully")
                st.write(response.text)
            else:
                st.error("Failed to generate report")

        except:
            st.error("Report service unavailable")

    st.info(
        "This module supports management reporting for "
        "inventory, supplier analysis, alerts, and forecasting."
    )

# --------------MAPS--------------
st.subheader("Logistics Tracking Map")

warehouse_location = [19.0760, 72.8777]  # Mumbai
supplier_location = [18.5204, 73.8567]   # Pune

m = folium.Map(
    location=warehouse_location,
    zoom_start=6
)

folium.Marker(
    warehouse_location,
    tooltip="Warehouse Location"
).add_to(m)

folium.Marker(
    supplier_location,
    tooltip="Supplier Location"
).add_to(m)

folium.PolyLine(
    [warehouse_location, supplier_location],
    tooltip="Delivery Route"
).add_to(m)

st_folium(m, width=700)
# -------------WAREHOUSE HEALTH------
st.subheader("Warehouse Health Score")

try:
    health_data = requests.get("http://127.0.0.1:5000/health").json()

    st.metric(
        label="Warehouse Health Score",
        value=f"{health_data['warehouse_health_score']}/100"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"🌡 Temperature: {health_data['temperature']} °C")
        st.write(f"📦 Low Stock Items: {health_data['low_stock_count']}")

    with col2:
        st.write(f"💧 Humidity: {health_data['humidity']} %")
        st.write(f"🚨 Critical Alerts: {health_data['critical_alerts']}")

except:
    st.error("Unable to fetch Warehouse Health Score")
