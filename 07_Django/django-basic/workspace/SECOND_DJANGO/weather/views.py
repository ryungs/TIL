from django.shortcuts import render, redirect
from .my_functions import get_weather
from .models import LocalWeather
# Create your views here.

def index(request):
    if request.method == 'GET':
        weathers = LocalWeather.objects.all()
        return render(request, 'weather/index.html/', { 'weathers': weathers })
    elif  request.method == 'POST':
        input_location = request.POST.get('input_location') #index.html의 input_location에서 온거
        weather = LocalWeather()
        if weather.get_weather(input_location):
            weather.save()
        return redirect('/weather')
        # data = get_weather(input_location)
        
        # weather = LocalWeather(
        #     location=input_location,
        #     lat=data[0], # 왜 data냐 get_weather(input_location)가 튜프롤 들어와서
        #     lon=data[1],
        #     temp=data[2],
        #     summary=data[3],
        #     search_time=data[4],
        # )
        # weather.save()
        # return redirect('/weather/')

def edit(request,id):
    weather = LocalWeather.objects.get(id=id)
    if request.method == 'GET':
        #HTML(weather/edit.html)
        return render(request, 'weather/edit.html/', {'weather': weather})
    else:
        # 수정 => 저장 => redirect '/weather/'
        weather.delete()
        weather.location = request.POST.get('input_location')
        data = get_weather(weather.location)
        
        weather = LocalWeather(
            location=weather.location,
            lat=data[0], # 왜 data냐 get_weather(input_location)가 튜프롤 들어와서
            lon=data[1],
            temp=data[2],
            summary=data[3],
            search_time=data[4],
        )
        weather.save()
        return redirect(f'/weather/')

def delete(request,id):
    #삭제 => redirect
    if request.method == 'POST':
        weather = LocalWeather.objects.get(id=id)
        weather.delete()
        return redirect ('/weather')
    
    else:
        return redirect (f'/weather/{id}/')