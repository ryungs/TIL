# 01 django basic→FIRST_DJANGO 

## 프레임워크

- 기본적인 구조나 필요한 코드들은 알아서 제공해줄게

- 넌 그냥 좋은 웹 서비스를 만들어

- 우리는 프레임워크를 사용할 것이다.

- React JS

  Ruby on Rails

  Python django

  PHP Laravel

  Java Spring



## django = m t v

= model + template + view

= 데이터 관리 / 사용자가 보는 화면/ 중간 관리



model templete

data base

- 다이어리에 그림 있음 중요한 



## FIRST_DJANGO 프로젝트 생성

- pip install django
- django-admin startproject first_django
- mv first_django/ FIRST_DJANGO
  - 대문자가 프로젝트 이름이다 app 이름이랑 같아서 대문자로 바꿔줌
- cd FIRST_DJANGO/
  - 항상  pwd는 대문자 프로젝트 이름!
- python manage.py runserver $IP:$PORT
  - manage.py 는 집사



#### setting.py  가서

```python
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = ['home',
    'etc',
    'artists',
    'workshop17',
]

'DIRS': [os.path.join(BASE_DIR, 'templates')],
    
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```



####  최상단 urls.py  가서

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('etc/', include('etc.urls')),
]
```



------



### 01. home app

#### urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('hi/<names>/', views.hi),
]
```



#### views.py

```python
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def hi(request, names):
    ss32 = [
        'dr',
        'yr',
        'st',
        'dg',
        'jy'
    ]
    return render(request, 'hi.html', {'name': names, 'ss3': ss32})
```



#### templates 안에 

- base.html
- index.html
- hi.html



------



### 02. etc app

#### urls.py

```python
from django.urls import path
from . import views


urlpatterns = [
    path('pick_lotto/', views.pick_lotto),
    path('square/<n>/', views.square),
]
```



#### views.py

```python
from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def pick_lotto(request):
    lotto = random.sample(range(1, 46), 6)
    return render(request, 'pick_lotto.html', { 'lotto': lotto })
    
def square(request, n):
    result = (int(n) ** 2)
    return  render(request, 'square.html', { 'num': int(n),'result': result })
```



#### templates 안에 

- base.html
- pick_lotto.html
- square.html



------

### 03. artist app

#### models.py

```python
from django.db import models

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=50)
    debut = models.IntegerField()
    is_active = models.BooleanField(default=True)
    description = models.TextField(default='No descriptions yet..')
    
def __str__(self):
    return f'{self.id}: {self.name}'
```

​                                                  