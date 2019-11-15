# ORM

#### cloud 9 → FIRST_DJANGO(프로젝트 생성) → artists(APP생성) → models.py에 예제 있음

#### bands

| id          | Integer   | PK       | AutoIncrement   |
| ----------- | --------- | -------- | --------------- |
| name        | Text(<50) | NOT NULL |                 |
| Debut       | INTEGER   |          | DEFAULT 1900    |
| Is_active   | Boolean   | NOT NULL | DEFAULT True    |
| Description |           |          | DEFAULT'......' |

- 스키마 만들기(sql로 했으면 테이블 만들겠지만 이제 sql 안씀)
- class 정의 (모델이 될 준비만 시킨 상태)
- 장고 안에 많은 class가 있지만 모두 모델이 되는 건 아니다

```django
from django.db import models

# Create your models here.
class Band(models.Model): # 필드 이름 정의 하고 상속받기
    name = models.CharField(max_length=50) #무조건 최대값 지정해줘야 한다
    debut = models.IntgerField()
    is_active = models.BooleanField(default=True)
    description = models.TextField(default='No description yet...')
```

- first_django → settings 에서 artists 등록하고
- python manage.py makemigrations artists 하면 이제 band가 model이 된거다

- python manage.py sqlmigrate artists 0001 이렇게 치면 이제 테이블 생성

-  python manage.py migrate : app 등록 

  

- 

- ctrl + d : shell 나가기 

- python manage.py dbshell

- python manage.py shell 

- from artists.models import Band

- Band.objects.all()
- Band.objects.get(id=1)
- Band.objects.filter(name__startswith='Qu')   



$ python manage.py createsuperuser