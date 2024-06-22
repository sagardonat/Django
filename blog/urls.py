from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('login', views.user_login , name='login'),
    path('accounts/login/', views.user_login , name='login'),
    path('logout', views.user_logout , name='logout'),
    path('signin', views.user_signin , name='signin'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),

]