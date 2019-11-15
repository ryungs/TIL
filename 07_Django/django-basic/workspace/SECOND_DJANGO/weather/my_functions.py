from IPython import embed # 얘는 함수 안에 없어도 된다, 디버깅 잡아주는 애

def get_weather(input_location):
    
    from darksky import forecast
    from geopy.geocoders import Nominatim
    from datetime import datetime
    
    API_KEY = 'd47b16e36ef06715e86efaf2f8753fb4'
    geo = Nominatim(user_agent='dr weather app')
    
   
    l = geo.geocode(input_location)
     #여기서 error 핸들링을 해라/models.py에서 class 밑에 넣어주고 if/else로 나눔
    lat = l.latitude
    lon = l.longitude
    location = forecast(API_KEY, lat, lon)
    temp = round((float(location.currently['temperature']) -32) * 5 / 9, 2)
    summary = location.currently['summary']
    t = datetime.utcfromtimestamp(location.time)
    return (lat, lon, temp, summary, t)
    
get_weather('멀티캠퍼스')
# embed()
