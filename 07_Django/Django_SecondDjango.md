# SECOND DJANGO

- 게시판 만들기

- 처음으로  mvt 를 다 만들어보는 프로젝트
- 원래 처음에 model 만들어줘야 함
- 프로젝트 생성 -> app 생성 -> 제일 상위 setting에서 app 등록 및 기타 세팅 바꾸고 ->

```python
django-admin startproject second-django
mv second_django SECOND_DJANGO
cd SECOND_DJANGO/
django-admin startapp boards
# second_django/settings.py/에서 app 등록
# second_django/boards/models.py에서 원하는 class 
python manage.py makemigrations boards #app 이름 꼭 쓰고
python manage.py migrate

# admin 사용자 만들기
python manage.py createsuperuser

# second_django/boards/admin.py 가서 밑에꺼 적고
from django.contrib import admin
from .models import Article
# Register your models here.
admin.site.register(Article)

python manage.py runserver $IP:$PORT
    
```



```python
 # 만들어진 table 보는 방법
 python manage.py dbshell
 . tables
```

```python
# table 날리는 방법
python manage.py migrate boards zero
```



```python
# app 날리는 방법
urls랑 app등록 된거 지우고 app 폴더 지우면 됨!
```

```python
# templates를 만들려면 templates 안에 자기 앱이름으로 mkdir을 만들어줘야 django 가 읽는다
mkdir -p board/templates/boards
```

```
boards/views.py 안에 
from django.shortcuts import render

# Create your views here.

# Create
    # user가 입력하는 창(html)
    return render(request)

    # user가 넘긴 데이터를 실제 DB에 저장하는 액션

# Read

    # index : 모든 article 들을 보여주는 html(목록)
    
    # 특정 article 을 보여주는 html(상세)
    
# Update
    # user가 입력하는 창(html)
    
    # user가 넘긴 데이터를 실제 DB에 저장하는 액션
    # Create와 차이는 처음 만들 때는 비어있지만 Update하려면 차 있는 상태에서 만들어진다
    
# Destory

    # 특정 article을 삭제하는 액션
```



view에서액션 먼저 만든다

- urls

- birthday 는 data 타입이라서 새로 넣어줘야함



### weather app 생성

- pip install django-extensions
  - 위에꺼 install 하면 python manage.py shell_plus 했을 때 더 쉽게 볼 수 있음
- app 등록
  - weather
  - django-extensions

- models.py  class LocalWeather 정의

- admin.py  admin 등록

  ```python
  from .models import LocalWeather
  # Register your models here.
  
  admin.site.register(LocalWeather)
  ```

- python manage.py makemigrations weather

- python manage.py migrate

- python manage.py runserver $IP:$PORT

```
- pip install darkskylib
- pip install geopy
  - weather에서 위치랑 날씨 받아오는 파일
- pip install ipython
  - 디버깅 잡아주는 파일
```



- my_funtions.py 에

  - from IPython import embed 추가해주고

  - embed() 하면 거기서 멈추고 디버깅 해줌

    

    

- python weather/my_funtions.py 해서 잘 나오는 지 확인!

```

```

- view.py 에서 def index 하고
- index.html 가서 for 문 작성
- base.html 가서 base 만들고 부트스트랩, 자바스트랩 링크 복사

- weather안에 urls.py 만들어서 맴핑해주고

- 최상단  urls.py 가서 weather안에 urls.py를 등록!

- index.html 가서 form 태그 작성 

  - action 은 아직 모르고
  - method는 POST

  - {% csrf_token %} 이거 꼭 쓰기!
  - table 태그로 만들고 for 문 작성

- 이제 submit에 넣으면 바로 가게 만들꺼야

- urls.py가서 search path 등록

- search가 없으니까 views 가서 만들다가.....

- def index(request): 를 다시 if elif로 나눔

- 이제 액션이 정해져서 index.html에 가서 action="/weather/ 로 바꿈

- search는 없앰...... 

- 돌려보다가 date time을 못받아옴!!

  - my_functions.py 가서 
  - from datetime import datetime
  - t = datetime.utcfromtimestamp(location.time)로 바꿔줌

- view.py에서 

  - elif  request.method == 'POST':
            input_location = request.POST.get('input_location') 가 잘못되었다면

  - 밑에 있는 이거를 받는게 아니라

    ```
    weather = LocalWeather(
                location=input_location,
                lat=data[0], # 왜 data냐 get_weather(input_location)가 튜프롤 들어와서
                lon=data[1],
                temp=data[2],
                summary=data[3],
                search_time=data[4],
            )
    ```

- my_fuctions.py에서 에러 핸들링은 힘드니까 나중에 하고
- 수정, 삭제만 만들기 끝!
- 