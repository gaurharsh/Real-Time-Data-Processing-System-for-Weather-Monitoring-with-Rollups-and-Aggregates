from django.db import models

# Django model (WeatherData) defines a database table for storing weather information
# Create your models he
class WeatherData(models.Model):
    city=models.TextField(max_length=50)
    date=models.DateField() #data was recorded uses DateField
    time=models.TimeField() #data was recorded  uses TimeField
    curr_temp=models.IntegerField()
    min_temp=models.IntegerField()
    max_temp=models.IntegerField()
    humidity=models.IntegerField()
    wind_speed=models.IntegerField()
    visibility=models.IntegerField()
    feels_like=models.IntegerField()

