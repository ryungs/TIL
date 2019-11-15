from django.urls import path
from . import views

urlpatterns = [
    path('articles/new_article/', views.new_article),
    path('articles/', views.index),
    path('articles/<int:id>/', views.detail),
    path('articles/delete/<int:id>/',views.delete),
    path('articles/update_article/<int:id>/', views.update_article),
    # path('articles/new/', views.new),
    # path('articles/create/', views.create),

