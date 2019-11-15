from django.urls import path
from . import views
# from . import views

urlpatterns = [
    path('pick_lotto/', views.pick_lotto),
    path('square/<n>/', views.square),
]
