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
API Key from OpenWeatherMap (Get one here)<be>
### The steps that need to be taken to execute this project on localhost
#### Step 1: Clone the repository<br>
		```
			git clone https://github.com/gaurharsh/weather_monitor.git
		```

#### Step 2: Create Virtual Environment By following command<br>
		```c
			python -m venv myweathermonitor
		```

#### Step 3: Activate virtual environment<br>
		
		```
			myweathermonitor\Scripts\activate.bat
		```
		
#### Step 4: Install requirements.txt<br>
		
		```
			pip install -r requirements. txt
		```
#### Step 5: locate manage.py and run<br>
		
		```
			cd weather_monitor
			python manage.py runserver
		```
  #### Step 6: Open your browser and visit: http://localhost:8000<br>

   ###Project Structure:
   
   weather_monitor/<br>
│
├── weather_monitor/           # Django project settings and URLs<br>
│   └── settings.py<br>
|   └── urls.py<br>
|   └── wsgi.py<br>
|   └── asgi.py<br>
|   └── _ _init__.py.py<br>
│<br>
├── weather_monitor_main/      # Main app handling weather monitoring<br>
│   ├── models.py              # Django models for storing weather data<br>
│   ├── views.py               # Main logic for fetching and displaying weather data<br>              
│   └── urls.py                # URL routes for the app<br>
│<br>
├──templates/                  # HTML templates for rendering the UI<br>
├── static/                    # Static files (CSS, JavaScript, images)<br>
├── db.sqlite3                 # SQLite database<br>
└── manage.py                  # Django management script<br>

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

Author
Harshvardhan
