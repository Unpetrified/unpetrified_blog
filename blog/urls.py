from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('post/<int:post_id>', views.Posts.as_view(), name='post'),
    path('register', views.Register.as_view(), name='register'),
    path('create/post', views.CreatePost.as_view(), name='create_post'),
    path('<int:post_id>', views.Comment.as_view(), name='comment'),
]
