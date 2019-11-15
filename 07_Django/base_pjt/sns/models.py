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
