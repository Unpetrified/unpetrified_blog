from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('post/<int:post_id>', views.Posts.as_view(), name='post'),
    path('register', views.Register.as_view(), name='register'),
    path('create/post', views.CreatePost.as_view(), name='create_post'),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('password/reset', auth_views.PasswordResetView.as_view(template_name='reset/reset.html'), name='password_reset'),
    path('password/reset/done', auth_views.PasswordResetDoneView.as_view(template_name='reset/reset_done.html'), name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset/reset_confirm.html'), name='password_reset_confirm'),
    path('<int:post_id>', views.Comment.as_view(), name='comment'),
]
