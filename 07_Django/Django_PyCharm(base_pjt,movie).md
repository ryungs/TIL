# PyCharm /base_pjt/movie

- input 태그 일일이 안써도 되게 만들어 봄!!
  - title, title_en, audience, genre, open_date 등등 이거 일일이 계속 다 썼는데
  - 한번만 적고 불러 오는 걸로 사용

- ctrl + shif + n : 파일 트리에서 파일 찾는 단축키
- 
- ctrl + f4 : 끄는거
- shif + enter

http://127.0.0.1:8000/movie/create/

```
student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ django-admin startapp movie

student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ touch movie/urls.py

student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ mkdir -p movie/templates/movie

```

```
# setting.py 가서
movie 등록하고

# models.py 가서
from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    title_eng = models.CharField(max_length=100)
    audience = models.ImageField(default=0)
    open_date = models.DateField()
    genre = models.CharField(max_length=100)
    watch_grade = models.CharField(max_length=100)
    score = models.FloatField(default=0.0)
    poster_url = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}: {self.title}'
```

```
student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ python manage.py makemigrations movie
Migrations for 'movie':
  movie\migrations\0001_initial.py
    - Create model Movie

student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ python manage.py migrate
```

```
#admin.py

from django.contrib import admin
from .models import Movie
# Register your models here.


class MovieModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Movie, MovieModelAdmin)
```

```
from django.shortcuts import render, redirect
from .models import Movie
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    return render(request, 'movie/list.html', {
        'movies': movies
    })

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        title_eng =request.POST.get('title_eng')
        audience = request.POST.get('audience')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        watch_grade = request.POST.get('watch_grade')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')

        Movie.objects.create(
            title=title,
            title_eng=title_eng,
            audience=audience,
            open_date=open_date,
            genre=genre,
            watch_grade=watch_grade,
            score=score,
            poster_url=poster_url,
            description=description,
        )

        return redirect('movie:list')

    else:
        return render(request, 'movie/create.html')
```

```
# app urls
from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.index, name='list'),
    path('create/', views.create, name='create'),
]

# 최상단 urls
 path('movie/', include('movie.urls')),
```

```
# base.html list.html. create.html 민ㄷ,ㅁ
# base.html 만들고

# create.html에서

{% extends 'movie/base.html' %}
{% block body %}
    <form method="POST">
        {% csrf_token %}
        제목 : <input type="text" name="title"> <br>
        영문 : <input type="text" name="title_eng"> <br>
        관객수 : <input type="text" name="audience"> <br>
        개봉일 : <input type="date" name="open_date"> <br>
        장르 : <input type="text" name="genre"> <br>
        상영등급 : <input type="text" name="watch_grade"> <br>
        평점 : <input type="text" name="score"> <br>
        포스터 url : <input type="text" name="poster_url"> <br>
        설명 : <textarea name="discription" cols="30" rows="10"></textarea><br>
        <input type="submit">
    </form>
{% endblock %}
```

```
# movie 안에 forms.py

from django import forms

class MovieForm(forms.Form):
    title = forms.CharField(max_length=100)
    title_eng = forms.CharField(max_length=100)
    audience = forms.ImageField()
    open_date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'})
    )
    genre = forms.CharField(max_length=100)
    watch_grade = forms.CharField(max_length=100)
    score = forms.FloatField()
    poster_url = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())
    
# form.py에는 TextField는 없다

```

```
# 다시 views.py 가서 form.py를 적용시켜보자

from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from IPython import embed

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movie/list.html', {
        'movies': movies
    })

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            title_eng = form.cleaned_data.get('title_eng')
            audience = form.cleaned_data.get('audience')
            open_date = form.cleaned_data.get('open_date')
            genre = form.cleaned_data.get('genre')
            watch_grade = form.cleaned_data.get('watch_grade')
            score = form.cleaned_data.get('score')
            # embed()
            poster_url = form.cleaned_data.get('poster_url')
            description = form.cleaned_data.get('description')

            Movie.objects.create(
                title=title, title_eng=title_eng, audience=audience,
                open_date=open_date, genre=genre, watch_grade=watch_grade,
                score=score, poster_url=poster_url, description=description,
            )
            return redirect('movie:list')
    else:
        form = MovieForm()

    return render(request, 'movie/create.html', {
        'form': form,
    })
```

```
# create.py 가서 원래 썼던거 없애고

{% extends 'movie/base.html' %}
{% block body %}
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>
{% endblock %}
```



```python
# forms.py가서 새로운 class MovieModelForm 생성

class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'  # ['title', 'title_eng'] 이렇게 원하는 것만 받을 수도 있다
        widgets = {
            'open_date': forms.DateInput(attrs={'type': 'date'})
        }
```

```
# views.py 가서
# from .forms import MovieModelForm 추가로 하고
# 원래 썼던거 다 주석처리하고 

from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm, MovieModelForm 

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movie/list.html', {
        'movies': movies
    })

def create(request):
    if request.method == 'POST':
        form = MovieModelForm(request.POST)
        if form.is_valid():
            # title = form.cleaned_data.get('title')
            # title_eng = form.cleaned_data.get('title_eng')
            # audience = form.cleaned_data.get('audience')
            # open_date = form.cleaned_data.get('open_date')
            # genre = form.cleaned_data.get('genre')
            # watch_grade = form.cleaned_data.get('watch_grade')
            # score = form.cleaned_data.get('score')
            # # embed()
            # poster_url = form.cleaned_data.get('poster_url')
            # description = form.cleaned_data.get('description')
            #
            # Movie.objects.create(
            #     title=title, title_eng=title_eng, audience=audience,
            #     open_date=open_date, genre=genre, watch_grade=watch_grade,
            #     score=score, poster_url=poster_url, description=description,
            # )
            form.save()
            return redirect('movie:list')
    else:
        form = MovieModelForm()

    return render(request, 'movie/create.html', {
        'form': form,
    })
```



