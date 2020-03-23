from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('list/', views.list),
    path('view/', views.view),
    path('average/', views.average),
    path('rate/', views.rate),
]