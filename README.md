# Real-Time-Data-Processing-System-for-Weather-Monitoring-with-Rollups-and-Aggregates
This project is a real-time weather monitoring dashboard built with Django. It fetches weather data from the OpenWeatherMap API and provides users with up-to-date<br> weather information and a 4-day forecast for multiple cities. The data includes temperature, humidity, wind speed, and weather alerts, with a dynamic user <br>interface displaying the conditions.<br>

## Features
##### Real-time weather data fetching for multiple cities.<br>
##### 4-day weather forecast.<br>
##### Detailed current weather information: temperature, humidity, wind speed, visibility, etc.<br>
##### Alerts for extreme weather conditions (e.g., rain, thunderstorms).<br>
##### Data storage in a SQLite database for further analysis.<br>
##### Responsive design using Bootstrap and Weather Icons.<br>
<br>
<br>

## Prerequisites<br>

#### Python 3.8+<br>
#### Django 5.1.2<br>
#### API Key from OpenWeatherMap (Get one here)<br>

### Setup Instructions

#### Step 1: Clone the repository<br>
		` ` ` cmd
			git clone https://github.com/gaurharsh/weather_monitor.git
		` ` `

#### Step 2: Create Virtual Environment By following command<br>
		```console
			python -m venv myweathermonitor
		```

#### Step 3: Activate virtual environment<br>
		
		```console
			myweathermonitor\Scripts\activate.bat
		```
		
#### Step 4: Install requirements.txt<br>
		
		```console
			pip install -r requirements. txt
		```
#### Step 5: locate manage.py and run<br>
		
		```console
			cd weather_monitor
			python manage.py runserver
		```
  #### Step 6: Open your browser and visit: http://localhost:8000<br>

   ### Project Structure:
   
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

## Key Files
#### 1. views.py: Contains the logic to fetch data from the OpenWeatherMap API and pass it to the frontend.<br>
#### 2. models.py: Defines the WeatherData model for saving weather data into the SQLite database.<br>
#### 3. index.html: The main template that renders weather information dynamically using Django’s templating engine.<br>

## Customization
#### Add more cities: In views.py, modify the cities list to include the cities you want to monitor.<br>
#### Modify forecast duration: Update the OpenWeatherMap API request in the get_forecast() function to extend or shorten the forecast period.<br>

## Static Files and Styling<br>
#### CSS is located in static/styles.css, and it includes references to external styles like FontAwesome and Weather Icons.<br>
#### Bootstrap is used for responsive layout design.<br>

## Future Improvements<br>
#### Add user authentication for personalized weather dashboards.<br>
#### Enable users to select and save their preferred cities.<br>
#### Implement weather alert notifications for severe weather conditions.<br>

## License<br>
This project is licensed under the MIT License. See the LICENSE file for details.<br>

## Author<br>
Harshvardhan<br>

## Screenshots
![ss1](/screenshots/Screenshot_1.png)<br>
![ss1](/screenshots/Screenshot_1.png)
