from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^orderflow/$', views.orderflow, name='orderflow'),
]