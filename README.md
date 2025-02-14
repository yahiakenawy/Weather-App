# Weather Monitoring Dashboard

A Flask-based web application that fetches and displays real-time weather data using the OpenWeatherMap API. The application includes temperature, humidity, and pressure monitoring with an interactive dashboard.

## Features
- **Real-time Data Collection:** Fetches weather data using the OpenWeatherMap API.
- **Automatic Data Scraping:** Configurable intervals for automatic data updates.
- **Interactive Charts:** Displays temperature, humidity, and pressure using Chart.js.
- **SQLite Database:** Stores weather data locally.
- **Responsive Dashboard:** A web interface that updates automatically.

## Prerequisites
- **Python 3.7+**
- **OpenWeatherMap API Key:** [Get one here](https://openweathermap.org/api)
- **Git**

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/weather-monitoring-dashboard.git
cd weather-monitoring-dashboard
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

### 4. Configure Your Environment
- Open `Config.py`
- Replace `API_KEY` with your OpenWeatherMap API key.
- Update `LATITUDE` and `LONGITUDE` with your desired location coordinates.

### 5. Initialize the Database
```bash
python Models.py
```

## Usage

### Start the Application
```bash
python App.py
```

Then, open your web browser and navigate to:

```
http://localhost:5000
```

The dashboard will automatically update every 10 seconds (this interval can be configured in `App.py`).

## Configuration
You can adjust the following settings in `Config.py`:
- `API_KEY`: Your OpenWeatherMap API key.
- `LATITUDE` and `LONGITUDE`: Location coordinates.
- `DATABASE_URI`: Database connection string.

To change the scraping interval, modify the `SCRAPING_INTERVAL` value in `App.py`.

## Project Structure
- **App.py:** Main Flask application and route handlers.
- **Config.py:** Configuration settings.
- **Models.py:** Database models and initialization.
- **Scraper.py:** Weather data fetching and storage.
- **templates/dashboard.html:** Frontend dashboard template.
- **environment.db:** SQLite database (created automatically).

## Contributing
1. Fork the repository.
2. Create your feature branch:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
