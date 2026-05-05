from main.apps import MainConfig
from main import views
from django.urls import path


app_name = MainConfig.name

urlpatterns = [
    path('', views.index, name='index'),
]