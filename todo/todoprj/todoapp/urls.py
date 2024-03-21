
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import delete_item, update_status

urlpatterns = [
   path('', views.home, name= 'home_page'),
   path('register/', views.register, name= 'register'),
   path('login/', views.loginpage, name= 'login'),
   path('create/', views.create, name= 'create'),
   path('current/', views.current, name= 'current'),
   path('completed/', views.completed, name= 'completed'),
   path('profile/', views.profile_view, name='profile'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   path('delete/<int:item_id>/', delete_item, name='delete_item'),
    path('update_status/<int:item_id>/', update_status, name='update_status'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)