from django.db import models

# Create your models here.
class LocalWeather(models.Model):
    location = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)
    temp = models.FloatField(default=0.0)
    summary = models.CharField(max_length=50)
    search_time = models.DateTimeField('date published')
    
    def get_weather(self, input_location):
        from darksky import forecast
        from geopy.geocoders import Nominatim
        from datetime import datetime
        
        API_KEY = 'd47b16e36ef06715e86efaf2f8753fb4'
        geo = Nominatim(user_agent='dr weather app')
        
   
        l = geo.geocode(input_location)
         #여기서 error 핸들링을 해라
        if l:
            self.lat = l.latitude
            self.lon = l.longitude
            self.location = input_location
            data = forecast(API_KEY, self.lat, self.lon)
            self.temp = round((float(location.currently['temperature']) -32) * 5 / 9, 2)
            self.summary = data.currently['summary']
            self.search_time = datetime.utcfromtimestamp(data.time)
            return Trune
        else:
            return False
    
    
    def __str__(self):
        return f'{self.id}: {self.location} @ {self.search_time}'
    