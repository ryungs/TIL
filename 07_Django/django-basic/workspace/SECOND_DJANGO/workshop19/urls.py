from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.index),
    path('students/<int:id>/', views.detail),
    path('students/new/', views.new),
    path('students/create/', views.create),
    path('students/delete/<int:id>/',views.delete),
    path('students/update_student/<int:id>/', views.update_student),
    ]