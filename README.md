🌦️ IoT Weather Monitoring System

This project simulates an IoT-based Weather Monitoring System. It includes both backend components (database + Flask) and a simple Tkinter GUI to visualize sensor readings.

--

##⚙️ Setup Steps

Clone the repository.

Create a virtual environment and install dependencies:

flask

matplotlib

pillow

sqlite3 (default in Python)

Set up the database:

Run sqlite3 weather.db < schema.sql to initialize tables.

Run the Tkinter simulation:

python3 tk_weather.py



---
##📊 How the Simulation Works

Sensors Emulated:

Temperature

Humidity

Pressure

The tk_weather.py file uses Tkinter to create a simple weather dashboard.

Values are randomly generated to simulate IoT sensor data.

--

##🛠️ Challenges Faced

Dependency mismatches with Flutter/Dart in the original repo.

Updated the project to run using Python + Tkinter instead of only Flutter.

Database permissions and missing schema.sql handling.


--

##🚀 Future Improvements

Integrate real IoT hardware (e.g., DHT11, BMP280 sensors).

Connect Tkinter dashboard directly with live database values.

Deploy a web-based dashboard (Flask + Charts).

Add mobile app support again with updated Flutter SDK.

✅ This repo now runs locally with Tkinter (tk_weather.py) so you can visualize sensor readings without external devices.
