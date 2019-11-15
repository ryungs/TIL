# Django-advance MYSITE 프로젝트 생성

## APP polls (설문조사 앱)

url 정리

-

-

-

-



#### polls models.py  처음으로 class 2개 만들어 봄

```python
from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 외부에 있는 다른 모델을 가르키겠다는 뜻
    # on_delete => Question이 날라갔을 때 밑에 모든 설문지는 날라간다
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(dafault=0)
```

#### ↓ 설명 1 : n = class Question : class Choice

| ID   | question_text    | pub_date |
| ---- | ---------------- | -------- |
| 1    | 중국집best       | 20190131 |
| 2    | 생일날 먹는 메뉴 | 20190131 |
|      |                  |          |

| Q_id | id   | choice_text | votes |
| ---- | ---- | ----------- | ----- |
| 2    | 1    | 짜장면      | 1     |
| 1    | 2    | 짜장면      | 20    |
| 1    | 3    | 치킨        | 1     |
| 2    | 4    | 볶음밥      | 3     |
| 1    | 5    | 아웃백      | 5     |
| 2    | 6    | 피자        | 7     |

