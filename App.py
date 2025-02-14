import threading
import time
from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import EnvironmentData
from Config import DATABASE_URI
from Scraper import fetch_weather_data, save_data  # Import scraper functions

app = Flask(__name__)

# Set up the database session for your Flask routes
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

# Adjustable scraping interval (in seconds)
# For example, set to 180 for 3 minutes or 600 for 10 minutes.
SCRAPING_INTERVAL = 86.5  # Change this value as desired

@app.route("/")
def index():
    session = Session()
    data_records = (
        session.query(EnvironmentData)
        .order_by(EnvironmentData.timestamp.desc())
        .limit(24)
        .all()
    )
    session.close()

    # Reverse to show data in chronological order (oldest first)
    data_records.reverse()

    # Prepare the data for the dashboard
    timestamps = [record.timestamp.strftime("%Y-%m-%d %H:%M:%S") for record in data_records]
    temperatures = [record.temperature for record in data_records]
    humidities = [record.humidity for record in data_records]
    pressures = [record.pressure for record in data_records]

    return render_template(
        "dashboard.html",
        timestamps=timestamps,
        temperatures=temperatures,
        humidities=humidities,
        pressures=pressures
    )

@app.route("/data")
def data():
    session = Session()
    data_records = (
        session.query(EnvironmentData)
        .order_by(EnvironmentData.timestamp.desc())
        .limit(24)
        .all()
    )
    session.close()

    data_records.reverse()

    timestamps = [record.timestamp.strftime("%Y-%m-%d %H:%M:%S") for record in data_records]
    temperatures = [record.temperature for record in data_records]
    humidities = [record.humidity for record in data_records]
    pressures = [record.pressure for record in data_records]

    return jsonify({
        "timestamps": timestamps,
        "temperatures": temperatures,
        "humidities": humidities,
        "pressures": pressures
    })

def run_scraper():
    """Background function to periodically fetch and save weather data."""
    while True:
        data = fetch_weather_data()
        if data:
            save_data(data)
        # Sleep for the duration defined by SCRAPING_INTERVAL
        time.sleep(SCRAPING_INTERVAL)

if __name__ == "__main__":
    # Start the scraper in a background daemon thread.
    scraper_thread = threading.Thread(target=run_scraper, daemon=True)
    scraper_thread.start()

    # Run the Flask application.
    app.run(debug=True)
