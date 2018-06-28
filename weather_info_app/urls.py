from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_city_weather/$', views.get_city_weather, name='get_city_weather'),
]