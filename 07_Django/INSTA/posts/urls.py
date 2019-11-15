from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new/', views.create_post, name='create_post'),
    path('<int:post_id>/edit/', views.update_post, name='update_post'),
    path('<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('<int:post_id>/comment/create/', views.create_comment, name='create_comment'),
    path('<int:post_id>/comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('<int:post_id>/like/', views.toggle_like, name='toggle_like'),
    # /insta/tag/hihi => hihi를 포함한 모든 post 보기
    path('tags/<str:tag_name>/', views.tag_posts_list, name='tag_posts_list'),
]