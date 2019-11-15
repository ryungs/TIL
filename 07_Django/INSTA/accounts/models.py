"""
장고 처음 시작할 때 밑에 5개를 먼저 하고 시작해라
0. User 모델 확장 가능성을 염두하라.
1. $ django-admin startproject MY_PROJECT
2. $ django-admin startapp accounts
3. accounts/models.py => 아래 코드 작성
4. settings.py => INSTALLED APPS += 'accounts'
5. settings.py => AUTH USERMODEL = 'accounts.User'
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    followings = models.ManyToManyField(
        settings.AUTH_USER_MODEL, # 스트링을 넣은거
        related_name='followers',
        blank=True,
        )
    # username, password, first_name, last_name, email

    def __str__(self):
        return self.username



