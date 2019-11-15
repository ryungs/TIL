from django.urls import path
from . import views

app_name = 'board_ad'

urlpatterns = [
    # Create
    path('new/', views.create_posting, name='create_posting'),

    # Read
    path('', views.posting_list, name='posting_list'), # Domain/postings
    path('<int:posting_id>/', views.posting_detail, name='posting_detail'), # Domain/postings/1

    # Update
    path('<int:posting_id>/edit/', views.update_posting, name='update_posting'),

    # Delete
    path('<int:posting_id>/delete/', views.delete_posting, name='delete_posting'),

    path('<int:posting_id>/comments/create/', views.create_comment, name='create_comment'),  # Domain/postings/1/comments/create
    path('<int:posting_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'), # Domain/postings/1/comments/1/delete
]