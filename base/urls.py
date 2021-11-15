from django.urls import path
from . import views

#List url paths
urlpatterns = [
    path('', views.homepage, name = "home"),
    path('room/<int:pk>', views.roompage, name = "room"),

]