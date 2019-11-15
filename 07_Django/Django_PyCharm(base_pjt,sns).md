# PyCharm /base_pjt/sns

- new project → Django →TIL- →07_Django →base_pjt



### 새로 배운 것들

- created_at, update_at 처음 만들어 봄

-  image = models.ImageField(blank=True) 쓰려면 pip install Pillow 해야함

- 프로젝트 안에 .gitignore  파일 만들어서

  ```
  venv/
  *.sqlite3
  .idea/
  __pycache__
  ```

- PyCharm 자동 인덴팅 :  Ctrl + Shift + Alt + L



```bash

student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ django-admin startapp sns

student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ touch sns/urls.py

student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ mkdir -p sns/templates/sns

student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ mkdir -p sns/static/sns

student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ pip install django-extensions

student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ python -m pip install --upgrade pip

student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ pip install ipython

```

```python
# setting.py 가서 기본 세팅하고
# 상위 urls 가서 등록
# app urls 가서 등록

# models.py 가서
from django.db import models


class Posting(models.Model):
    content = models.CharField(max_length=500)
    icon = models.CharField(max_length=20, default='fas fa-question') 
    # font awesome 약자
    image = models.ImageField(blank=True)
    
    def __str__(self): # 이렇게 선언해줘야 admin 페이지에서 위치값이 아닌 우리가 보기 좋게 나온다
        return f'{self.id}: {self.content[:10]}'


class Comment(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.id}: {self.content}'
```

```bash
student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ python manage.py makemigrations sns
SystemCheckError: System check identified some issues:

ERRORS:
sns.Posting.image: (fields.E210) Cannot use ImageField because Pillow is not installed.
        HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "pip install Pillow".

# ImageField 쓰려면 install Pillow 해야함

student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ pip install Pillow


student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ python manage.py makemigrations sns


student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$   python manage.py migrate


student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ python manage.py createsuperuser
```



### Python Console 에서

```shell
from sns.models import Posting
from sns.models import Comment
p = Posting()
p = Posting(content='Hi')
p.content = 'adjifojweijflkdsjfsiefjlksd'
p
Out[8]: <Posting: None: adjifojwei>
p.save()
p
Out[10]: <Posting: 1: adjifojwei> 

# return f'{self.id}: {self.content[:10]}' 잘 나오는지 확인        
```

```python
# 다시 models.py
from django.db import models
from datetime import datetime

class Posting(models.Model):
    content = models.CharField(max_length=500)
    icon = models.CharField(max_length=20, default='fas fa-question') # font awesome 약자
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now)

    def __str__(self): # 이렇게 선언해줘야 admin 페이지에서 위치값이 아닌 우리가 보기 좋게 나온다
        return f'{self.id}: {self.content[:10]}'


class Comment(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now)

    def __str__(self):
        return f'{self.id}: {self.content}'
```

```bash
student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ python manage.py makemigrations sns
You are trying to add the field 'created_at' with 'auto_now_add=True' to comment without a default; the database needs something to populate existing rows.

 1) Provide a one-off default now (will be set on all existing rows)
 2) Quit, and let me add a default in models.py
Select an option: 2
 
# created_at에서 default 값 때문에 에러남
# 나중에 추가하려고 하면 작업 엄청 복잡하니까 이제부터 created_at, updated_at 항상 먼저 해줘라!!
```

```bash
# models.py에서  default=datetime.now 지우고

student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ python manage.py migrate sns zero

# zero 해준 다음에
```

```python
# 다시 models.py
from django.db import models
from datetime import datetime

class Posting(models.Model):
    content = models.CharField(max_length=500)
    icon = models.CharField(max_length=20, default='fas fa-question') # font awesome 약자
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): # 이렇게 선언해줘야 admin 페이지에서 위치값이 아닌 우리가 보기 좋게 나온다
        return f'{self.id}: {self.content[:10]}'


class Comment(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # created_at, updated_at 는 처음부터 무조건 넣는다고 생각하기

    def __str__(self):
        return f'{self.id}: {self.content}'
       
```

```bash
student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ python manage.py makemigrations sns


student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ python manage.py migrate

```

```python
# admin.py 가서

from django.contrib import admin
from .models import Posting, Comment
# Register your models here.


class PostingModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Posting, PostingModelAdmin)


class CommentModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Comment, CommentModelAdmin)
```

```bash
student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ python manage.py runserver
```

```python
# app urls.py

from django.urls import path
from . import views

app_name = 'sns'

urlpatterns = [
    path('', views.posting_list, name='posting_list'),
    path('<int:posting_id>/', views.posting_detail, name='posting_detail'),
    path('new/', views.create_posting, name='create_posting'),
    path('<int:posting_id>/edit/', views.edit_posting, name='edit_posting'),
    path('<int:posting_id>/delete/', views.delete_posting, name='delete_posting'),
]
```

```python
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Posting, Comment
# Create your views here.

def posting_list(request):
    pass

def posting_detail(request):
    pass

def create_posting(request):
    pass

def edit_posting(request):
    pass

def delete_posting(request):
    pass
```

```html
<!--  base.html, list.html, detail.html 만듬 -->
    
<!-- base.html -->
<!doctype html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.1/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <title>My SNS</title>
</head>
<body>
    <ul class="nav nav-tabs">
        <li class="nav-item">
            <a href="{% url 'sns:posting_list' %}" class="nav-link">Timeline</a>
        </li>
        <li class="nav-item">
            <a class="nav-link">Detail</a>
        </li>
    </ul>
    <div class="container">
        {% block  %}
        {% endblock %}
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
</body>
</html>
```

```html
<!--  _nav.html 에서 active aria-disabled="true" 추가하면 
 http://127.0.0.1:8000/sns/에서 마치 그 페이지에 가있는 것 처럼 뜬다 -->

<ul class="nav nav-tabs">
    <li class="nav-item">
        <a href="{% url 'sns:posting_list' %}" class="nav-link active">Timeline</a>
    </li>
    <li class="nav-item">
        <a class="nav-link" aria-disabled="true">Detail</a>
    </li>
</ul>

```

```html
<!--  list.html 가서 -->
{% extends 'sns/base.html' %}

{% block body %}
    {% include 'sns/_header.html' %}

{% endblock %}

#_header.html
<header>
    <form action="{% url 'sns:create_posting' %}" method="POST" enctype="multipart/form-data">
    <!-- 파일 넣으려면 enctype="multipart/form-data" 이거 무조건 적어줘야함 -->
        {% csrf_token %}
        <div class="form-row align-items-center">
            <!-- icon select tag -->
            <div class="col-auto my-1">
                <label for="icon" class="sr-only">icon</label>
                <select name="icon" id="icon" class="custom-select mr-sm-2">
                    <option value="fas fa-question">?</option>
                    <option value="far fa-smile">:)</option>
                    <option value="far fa-angry">:(</option>
                    <option value="far fa-smile-wink">;)</option>
                </select>
            </div>

            <!-- content input tag -->
            <div class="col-sm-6 my-1">
                <label for="content" class="sr-only">content</label>
                <input type="text" name="content" id="content" class="form-control" placeholder="Feels like..">
            </div>

            <!-- image file input tag -->
            <div class="col-sm-4 my-1 input-group">
                <div class="input-group-prepend">
                    <span class="input-group-text">Upload</span>
                </div>
                <div class="custom-file">
                    <input id="image" class="custom-file-input" name="image" type="file" accept="image/*">
                    <label for="image" class="custom-file-label">Choose image</label>
                </div>
            </div>

            <!-- submit button -->
            <div class="col-auto my-1">
                <button type="submit" class="btn btn-primary">Submit</button>
            </div>
        </div>
    </form>
</header>
```

```python
# view.py 가서

def create_posting(request):
    if request.method == 'POST':
        posting = Posting()
        posting.content = request.POST.get('content')
        posting.icon = request.POST.get('icon')
        posting.image = request.FILES.get('image')
        posting.save()
        return redirect('sns:posting_detail', posting.id)
    else:
        return redirect('sns:posting_list')
```

```python
# view.py 가서

def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)

    return render(request, 'sns/detail.html', {
        'posting': posting,
    })
```

```html
<!--  detail.html 가서 -->

{% extends 'sns/base.html' %}

{% block body %}
    <div class="row mt-3">
        <div class="col-12 col-md-6">
            <div class="card">
                <img src="http://lorempixel.com/g/200/300" class="card-image-top" alt="random_image">
                <div class="card-body">
                    <i class="{{ posting.icon }}"></i>
                    <hr>
                    <p class="card-text">{{ posting.content }}</p>
                </div>
            </div>

            <div class="card mt-2">
                <div class="card-body">
                    <form action="#" method="POST">
                        {% csrf_token %}
                        <label for="comment">leave comment</label>
                        <input type="text" name="comment" id="comment" class="form-control">
                    </form>
                </div>
            </div>

        </div>
  
{% endblock %}

<!-- 여기서 comments 보여주려고 하니까 view.py 가서 detail에 comment 인자가 안들어가 있기 때문에 -->
```

```python
#view.py 가서 detail에 comments 추가하고

def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comment_set.all()
    return render(request, 'sns/detail.html', {
        'posting': posting,
        'comments': comments,
    })
```



```html
<!-- detail.html 가서 페이지 레이아웃 완성하는데 <div class="card-body">안에 class="form-control" 넣어줘야 -->

{% extends 'sns/base.html' %}

{% block detail %}active{% endblock %}
{% block body %}
    <div class="row mt-3">
        <div class="col-12 col-md-6">
            <div class="card">
                <img src="http://lorempixel.com/g/200/300" class="card-image-top" alt="random_image">
                <div class="card-body">
                    <i class="{{ posting.icon }}"></i>
                    <hr>
                    <p class="card-text">{{ posting.content }}</p>
                </div>
            </div>

            <div class="card mt-2">
                <div class="card-body">
                    <form action="#" method="POST">
                        {% csrf_token %}
                        <label for="comment">leave comment</label>
                        <input type="text" name="comment" id="comment" class="form-control">
                    </form>
                </div>
            </div>

        </div>
        <div class="col-12 col-md-6">
            <div class="card">
                <ul class="list-group list-group-flush">
                    {% if comments %}
                        {% for comment in comments %}
                            <li class="list-group-item mb-1">{{ comment.content }}</li>
                        {% endfor %}
                    {% else %}
                        <li class="list-group-item mb-1">No comments yet...</li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </div>
{% endblock %}
```

```html
<!-- 근데 detail 페이지 갔을 때 위에있는 active가 Timeline에서 detail로 옮겨지게 하고 싶기 때문에 _nav.html에 가서 active를 지우고 각각 a 태그 안에 펀칭 내주고 -->

<ul class="nav nav-tabs">
    <li class="nav-item">
        <a href="{% url 'sns:posting_list' %}" class="nav-link {% block list %}{% endblock %}">Timeline</a>
    </li>
    <li class="nav-item">
        <a class="nav-link {% block detail %}{% endblock %}" aria-disabled="true">Detail</a>
    </li>
</ul>
```

```html
<!-- list.html 상단에 가서 펀칭 맴핑시켜주고 -->
{% extends 'sns/base.html' %}
{% block list %}active{% endblock %}

<!-- detail.html 상단에 가서 펀칭 맴핑시켜주고 -->
{% extends 'sns/base.html' %}
{% block detail %}active{% endblock %}
```

```html
<!-- list.html에서 페이지 레이아웃 잡아주는데 img 태그 안에 alt="random_img{{ forloop.counter }}를 이렇게 넣는거 주의하기 -->

{% extends 'sns/base.html' %}
{% block list %}active{% endblock %}

{% block body %}
    {% include 'sns/_header.html' %}
    <hr>
    {% if postings %}
        <section class="row mt-5">
        {% for posting in postings %}
            <article class="col-12 col-md-3">
                <div class="card mb-2">
                    <a href="{% url 'sns:posting_detail' posting.id %}">
                        <img src="http://lorempixel.com/g/150/75" class="card-img-top" alt="random_img{{ forloop.counter }}">
                    </a>
                    <div class="card-body">
                        <i class="{{ posting.icon }}"></i>
                    </div>
                </div>
            </article>
        {% endfor %}

        </section>
    {% endif %}
{% endblock %}
```

```html
<!-- detail.html 가서 이미지가 있을 때는 내가 올린 이미지 이미지가 없을 때는 랜덤 이미지 내놓게 하려고 img 태그 안에 if else로 나눠서 코드 수정함 -->

<!-- img 태그 class 안에 image-fluid 넣어주면 가로폭 고정됨 -->


{% extends 'sns/base.html' %}
{% block detail %}active{% endblock %}

{% block body %}
    <div class="row mt-3">
        <div class="col-12 col-md-6">
            <div class="card">
                {% if posting.image %}
                    <img src="{{ posting.image.url }}" class="card-img-top image-fluid" alt="{{ posting.image }}">
                {% else %}
                    <img src="http://lorempixel.com/g/200/300" class="card-image-top image-fluid" alt="random_image">
                {% endif %}

                <div class="card-body">
                    <i class="{{ posting.icon }}"></i>
                    <hr>
                    <p class="card-text">{{ posting.content }}</p>
                </div>
            </div>

            <div class="card mt-2">
                <div class="card-body">
                    <form action="#" method="POST">
                        {% csrf_token %}
                        <label for="comment">leave comment</label>
                        <input type="text" name="comment" id="comment" class="form-control">
                    </form>
                </div>
            </div>

        </div>
        <div class="col-12 col-md-6">
            <div class="card">
                <ul class="list-group list-group-flush">
                    {% if comments %}
                        {% for comment in comments %}
                            <li class="list-group-item mb-1">{{ comment.content }}</li>
                        {% endfor %}
                    {% else %}
                        <li class="list-group-item mb-1">No comments yet...</li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </div>
{% endblock %}

```



```python
# 위에 처럼 img 태그 안에 if, else로 나오게 하려면 수정해줘야 하는 것들이 있다

# setting.py가서 제일 마지막에 2줄 추가
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 최상단 urls.py 가서 3줄 추가
from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

```html
<!-- list.html 가서도 가서 이미지가 있을 때는 내가 올린 이미지 이미지가 없을 때는 랜덤 이미지 내놓게 하려고 img 태그 안에 if else로 나눠서 코드 수정함 -->

<!-- img 태그 class 안에 image-fluid 넣어주면 가로폭 고정됨 -->

{% extends 'sns/base.html' %}
{% block list %}active{% endblock %}

{% block body %}
    {% include 'sns/_header.html' %}
    <hr>
    {% if postings %}
        <section class="row mt-5">
        {% for posting in postings %}
            <article class="col-12 col-md-3">
                <div class="card mb-2">
                    <a href="{% url 'sns:posting_detail' posting.id %}">
                        {% if posting.image %}
                            <img src="{{ posting.image.url }}" class="card-img-top image-fluid" alt="{{ posting.image }}">
                        {% else %}
                            <img src="http://lorempixel.com/g/150/75" class="card-img-top image-fluid" alt="random_img{{ forloop.counter }}">
                        {% endif %}

                    </a>
                    <div class="card-body">
                        <i class="{{ posting.icon }}"></i>
                    </div>
                </div>
            </article>
        {% endfor %}

        </section>
    {% endif %}
{% endblock %}
```

```
# .gitignore 에 추가
media/
```

```html
<!-- list.html에서 image를 크기대로 저절로 붙이게 하는 코드 -->
<section class="row mt-5">
 <article class="col-12 col-md-3">
{% extends 'sns/base.html' %}
{% block list %}active{% endblock %}

{% block body %}
    {% include 'sns/_header.html' %}
    <hr>
    {% if postings %}
        <section class="card-columns">
            {% for posting in postings %}
                <article class="card mb-2">
                    <a href="{% url 'sns:posting_detail' posting.id %}">
                        {% if posting.image %}
                            <img src="{{ posting.image.url }}" class="card-img-top image-fluid"
                                 alt="{{ posting.image }}">
                        {% else %}
                            <img src="http://lorempixel.com/g/150/75" class="card-img-top image-fluid"
                                 alt="random_img{{ forloop.counter }}">
                        {% endif %}

                    </a>
                    <div class="card-body">
                        <i class="{{ posting.icon }}"></i>
                    </div>
                </article>
            {% endfor %}

        </section>
    {% endif %}
{% endblock %}

```

```python
# app urls.py 가서 create_comment url 추가


path('<int:posting_id>/comments/create/', views.create_comment, name='create_comment')
```

```python
# views.py 가서 def create_comment 추가

def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.method == 'POST':
        comment = Comment()
        comment.content = request.POST.get('comment')
        comment.posting = posting
        comment.save()
        return redirect('sns:posting_detail', posting_id)
```

```html
<!-- detail.html 가서 form 태그에 action을 reate_comment로 맵핑 -->

<div class="card mt-2">
                <div class="card-body">
                    <form action="{% url 'sns:create_comment' posting.id %}" method="POST">
                        {% csrf_token %}
                        <label for="comment">leave comment</label>
                        <input type="text" name="comment" id="comment" class="form-control">
                    </form>
                </div>
            </div>
```

```html
<!-- 댓글 갯수만큼 list 페이지에서 아이콘 갯수 늘리고 싶으면 list.html 가서 추가 -->
<div class="card-body">
                        {% if posting.comment_set.count < 5 %}
                            {% for i in posting.comment_set.all %}
                                <i class="{{ posting.icon }} fa-1x"></i>
                            {% endfor %}
                        {% else %}
                            <i class="{{ posting.icon }} fa-1x"></i> x {{ posting.comment_set.count }}
                        {% endif %}
                    </div>
```

```bash
# 가상환경에 깔려 있는 것들 리스트 txt로 만들어줌
pip freeze > requirements.txt

# 리스트에 있는거 한번에 설치할 때
pip install -r requirements.txt
```





