from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('login/', views.loginPage, name='loginPage'),
    path('register/', views.register, name='register'),
]
