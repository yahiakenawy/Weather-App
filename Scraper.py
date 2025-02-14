# scraper.py
import datetime
import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from Config import API_KEY, WEATHER_API_URL, LATITUDE, LONGITUDE, DATABASE_URI
from Models import EnvironmentData, init_db

def fetch_weather_data():
    params = {
        "lat": LATITUDE,
        "lon": LONGITUDE,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(WEATHER_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        return {
            "temperature": temperature,
            "humidity": humidity,
            "pressure": pressure,
            "weather_description": weather,
            "timestamp": datetime.datetime.utcnow()
        }
    else:
        print("Error fetching data:", response.status_code)
        return None

def save_data(data):
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker(bind=engine)
    session = Session()
    env_data = EnvironmentData(
        temperature=data["temperature"],
        humidity=data["humidity"],
        pressure=data["pressure"],
        weather_description=data["weather_description"],
        timestamp=data["timestamp"]
    )
    session.add(env_data)
    session.commit()
    session.close()
    print("Data saved at", data["timestamp"])

if __name__ == "__main__":
    # Initialize the database (if not already)
    engine = init_db()
    # Fetch and save data
    data = fetch_weather_data()
    if data:
        save_data(data)
