# Real-Time-Data-Processing-System-for-Weather-Monitoring-with-Rollups-and-Aggregates
This project is a real-time weather monitoring dashboard built with Django. It fetches weather data from the OpenWeatherMap API and provides users with up-to-date weather information and a 4-day forecast for multiple cities. The data includes temperature, humidity, wind speed, and weather alerts, with a dynamic user interface displaying the conditions.

Features
Real-time weather data fetching for multiple cities.
4-day weather forecast.
Detailed current weather information: temperature, humidity, wind speed, visibility, etc.
Alerts for extreme weather conditions (e.g., rain, thunderstorms).
Data storage in a SQLite database for further analysis.
Responsive design using Bootstrap and Weather Icons.


Prerequisites
Python 3.8+
Django 5.1.2
API Key from OpenWeatherMap (Get one here)

Installation
1. Clone the repository:
   git clone https://github.com/yourusername/weather_monitor.git
cd weather_monitor

2. Install required Python packages:
    pip install -r requirements.txt
3. Set up your OpenWeatherMap API key in the Django project:
    Open views.py and update the api_key variable with your OpenWeatherMap API key.
4. Run migrations to set up the SQLite database:
    python manage.py migrate
5. Run the development server:
   python manage.py runserver

6. Open your browser and visit: http://localhost:8000

   Project Structure:
   weather_monitor/
│
├── weather_monitor/           # Django project settings and URLs
│   └── settings.py
│
├── weather_monitor_main/      # Main app handling weather monitoring
│   ├── models.py              # Django models for storing weather data
│   ├── views.py               # Main logic for fetching and displaying weather data
│   ├── templates/             # HTML templates for rendering the UI
│   ├── static/                # Static files (CSS, JavaScript, images)
│   └── urls.py                # URL routes for the app
│
├── db.sqlite3                 # SQLite database
└── manage.py                  # Django management script

Key Files
1. views.py: Contains the logic to fetch data from the OpenWeatherMap API and pass it to the frontend.
2. models.py: Defines the WeatherData model for saving weather data into the SQLite database.
3. index.html: The main template that renders weather information dynamically using Django’s templating engine.

Customization
Add more cities: In views.py, modify the cities list to include the cities you want to monitor.
Modify forecast duration: Update the OpenWeatherMap API request in the get_forecast() function to extend or shorten the forecast period.

Static Files and Styling
CSS is located in static/styles.css, and it includes references to external styles like FontAwesome and Weather Icons.
Bootstrap is used for responsive layout design.

Future Improvements
Add user authentication for personalized weather dashboards.
Enable users to select and save their preferred cities.
Implement weather alert notifications for severe weather conditions.

License
This project is licensed under the MIT License. See the LICENSE file for details.
