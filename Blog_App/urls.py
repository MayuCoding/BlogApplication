# define urls for the Blog_App

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('article/<slug:slug>/', views.read, name='read'),
    path('article/<slug:slug>/update/', views.update, name='update'),
    path('article/<slug:slug>/delete/', views.delete, name='delete'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),

]