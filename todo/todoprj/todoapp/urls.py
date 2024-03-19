
from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name= 'home_page'),
   path('register/', views.register, name= 'register'),
   path('login/', views.loginpage, name= 'login'),
   path('create/', views.create, name= 'create'),
   path('current/', views.current, name= 'current'),
   path('completed/', views.completed, name= 'completed'),
]