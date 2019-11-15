from django.contrib import admin
from .models import Article

# Register your models here.

# Article 모델을 admin site에서 등록해서 확인하래!
admin.site.register(Article)
