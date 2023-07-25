from . import views
from django.urls import path

urlpatterns=[
    path("", views.RegisterPage, name='registerpage'),
    path('register/', views.User_Register, name='register'),
    path('final/', views.final, name='final')
]