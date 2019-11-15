# PyCharm /base_pjt/accounts

### 로그인 페이지 만들기



````
student@M70324 MINGW64 ~/TIL/07_Django/base_pjt (master)
$ django-admin startapp accounts
```

```
# setting.py 가서 앱등록

# app urls.py 만들어서
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns =[
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
]

# 최상단 urls 가서 추가
path('accounts/', include('accounts.urls')),


# view.py 가서 추가하기
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')

def signup(request):
    # 사용자가 실제 데이터를 제출했다면 저장한 다음에
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:index')
    # 사용자가 가입하겠다고 들어오면 보여줄 html
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })

def signin(request):
    pass

def signout(request):
    pass



# signup.html index.html 2개 만듬
# signup.html에

<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
</form>

```

```
python manage.py runserver 해서
http://127.0.0.1:8000/accounts/signup/ 들어가면
회원가입 페이지가 뜸
회원가입하고 
http://127.0.0.1:8000/admin 가면
사용자들에 방금 회원가입한 아이디가 추가되어 있음

알고리즘: pbkdf2_sha256 반복: 120000 솔트: Sp4K6o****** 해시: jihvkV**************************************
이런식으로 비밀번호가 저장되서 관리자도 비밀번호 모른다

```







http://127.0.0.1:8000/accounts/signup/

```
# views.py def signin, def signout 추가 해주고
def signin(request):
    # 이미 로그인 했는데 또 로그인 한다하면,
    if request.user.is_authenticated:
        return redirect('accounts:index')

    # 로그인 시켜주세요
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('accounts:index')

    # 로그인 화면주세요
    else:
        form = AuthenticationForm
    return render(request, 'accounts/signup.html',{
      'form':form
    })
def signout(request):
    logout(request)
    return redirect('accounts:index')
```

```
# index.html 에 a 태그 추가해주고

<h1>회원가입과 로그인 테스트</h1>

<h2>
    {% if user.is_authenticated %}
    You are LOGGED IN! <a href="{% url 'accounts:signout' %}">로그아웃 하러가기</a>
    {% else %}
    You are Not LOGGED IN... <a href="{% url 'accounts:signin' %}">로그인 하러가기</a>
    {% endif %}
</h2>
```

```
# sign.html , signup.html

<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
</form>
```

```
# 로그인 페이지와 무비 페이지를 연결하려면
# movie의 views.py 가서
from django.contrib.auth.decorators import login_required 하고

# def create 위에 login_required 추가하고

@login_required(login_url='/accounts/signin')
def create(request):
    if request.method == 'POST':
        form = MovieModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie:list')
    else:
        form = MovieModelForm()

    return render(request, 'movie/create.html', {
        'form': form,
    })
    

# accounts의 views.py 가서 변경


def signin(request):
    # 이미 로그인 했는데 또 로그인 한다하면,
    if request.user.is_authenticated:
        return redirect('accounts:index')

    # 로그인 시켜주세요
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid(): # 검증 성공
            login(request, form.get_user()) # 로그인 하고

            if request.GET.get('next'): # 이전에 있던 페이지가 있다면
                return redirect(request.GET.get('next'))
            return redirect('accounts:index')
    # 로그인 화면주세요
    else:
        form = AuthenticationForm
    return render(request, 'accounts/signup.html',{
      'form':form
    })

```

