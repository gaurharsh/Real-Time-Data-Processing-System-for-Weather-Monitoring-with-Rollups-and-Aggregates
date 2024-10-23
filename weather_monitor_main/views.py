from django.shortcuts import render
from .models import WeatherData
import requests
import datetime
import math
# Create your views here.def index(request):
def get_dayname(unix_timestamp):#convert unix timestamp to human readable day name
    dt = datetime.datetime.fromtimestamp(unix_timestamp)
    return dt.strftime("%A")

def get_forecast(city): # Function to Get Weather Forecast
    url = f"https://api.openweathermap.org/data/2.5/forecast/daily?APPID=9b4bbf30228eb8528d36e79d05da1fac&q={city}&units=metric&cnt=5"
    response = requests.get(url)
    data = response.json()
    forecast_data = {}
    fore=[]
    weatherIconsMap = {"01d": "wi-day-sunny","01n": "wi-night-clear","02d": "wi-day-cloudy","02n": "wi-night-cloudy","03d": "wi-cloud","03n": "wi-cloud","04d": "wi-cloudy","04n": "wi-cloudy","09d": "wi-showers","09n": "wi-showers","10d": "wi-day-hail","10n": "wi-night-hail","11d": "wi-thunderstorm","11n": "wi-thunderstorm","13d": "wi-snow","13n": "wi-snow","50d": "wi-fog","50n": "wi-fog"}
    try:
        for i in range(1,5):
            temp=[]
            temp.append(data["list"][i]["temp"]["day"])
            temp.append(data["list"][i]["temp"]["night"])
            temp.append(data["list"][i]["temp"]["eve"])
            temp.append(data["list"][i]["temp"]["morn"])
            avg=math.ceil(sum(temp)/len(temp))
            mint=data["list"][i]["temp"]["min"]
            maxt=data["list"][i]["temp"]["max"]
            day_name=get_dayname(data["list"][i]["dt"])
            icn=data["list"][i]["weather"][0]["icon"]
            fore.append({"avg":avg,"min":mint,"max":maxt,"day_name":day_name[0:3],"icon":weatherIconsMap[icn]})
        for i in range(0,len(fore)):
            forecast_data[i]=fore[i]
        return forecast_data
    except KeyError:
        return "CityNotFound:invalid city name"
def AckAlert(WeatherCond):
    condition_lis=["Haze","Rain","Thunderstorm","Fog","Clouds","Atmosphere","Drizzle","Snow","Smoke"]
    if WeatherCond in condition_lis:
        return True
    else:
        return False
def index(request):
    api_key = "5d6340fd102e2b7ff8556f85530790e7"
    cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d")
    formatted_time = now.strftime("%I:%M %p")
    date1=formatted_date
    time1=formatted_time
    time2=now.strftime("%I:%M")
    date2=now.strftime("%A, %B %d, %Y")
    weatherdata=[]
    weatherIconsMap = {"01d": "wi-day-sunny","01n": "wi-night-clear","02d": "wi-day-cloudy","02n": "wi-night-cloudy","03d": "wi-cloud","03n": "wi-cloud","04d": "wi-cloudy","04n": "wi-cloudy","09d": "wi-showers","09n": "wi-showers","10d": "wi-day-hail","10n": "wi-night-hail","11d": "wi-thunderstorm","11n": "wi-thunderstorm","13d": "wi-snow","13n": "wi-snow","50d": "wi-fog","50n": "wi-fog"}
    try:
        for city in cities:
            #get data from api and show on template
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            data = response.json()
            foredata=get_forecast(city)
            weatherdata.append({
                "icon":weatherIconsMap[data["weather"][0]["icon"]],
                "location": city,
                "date":date2,
                "time":time1,
                "temp": math.ceil(data["main"]["temp"]),
                "max_temp":math.ceil(data["main"]["temp_max"]),
                "min_temp":math.ceil(data["main"]["temp_min"]),
                "feels_like": math.ceil(data["main"]["feels_like"]),
                "wind":round(data["wind"]["speed"],2),  
                "condition": data["weather"][0]["main"],
                "condition_des": data["weather"][0]["description"],
                "humidity":data["main"]["humidity"],
                "visibility":round(data["visibility"]/1000,2),
                "foredata":foredata,
                "Alert":AckAlert(data["weather"][0]["main"])
             })
            #store data in database for furthrr analysis
            weather__data=WeatherData(
                city=city,
                date=date1,
                time=time2,
                curr_temp=math.ceil(data["main"]["temp"]),
                min_temp=math.ceil(data["main"]["temp_min"]), 
                max_temp=math.ceil(data["main"]["temp_max"]),
                humidity=data["main"]["humidity"],
                wind_speed=round(data["wind"]["speed"],2),
                visibility=round(data["visibility"]/1000,2),
                feels_like=math.ceil(data["main"]["feels_like"])
                )
 
            weather__data.save()
    except KeyError:
        return render(request,'index.html',{"ErrFlag":True,"ErrVal":{"main":"CityNotFound:invalid city name","Fcast":get_forecast(city)}})
    return render(request,'index.html',{"weatherdata":weatherdata})