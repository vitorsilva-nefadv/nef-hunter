from django.urls import path
from . import views

app_name = "huntering"

#Usar app_name ajuda no namespacing
urlpatterns = [
    path("", views.home, name="home"),
]