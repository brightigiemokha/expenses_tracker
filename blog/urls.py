
from django.urls import path
from  . import views

urlpatterns = [
    path('', views.test),
    path('loginn/', views.loginn),
    path('signup', views.signup)
]
