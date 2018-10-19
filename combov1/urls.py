from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^orderv1/$', views.order, name='orderv1')
]