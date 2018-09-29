from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^view/$', views.combo, name='combo'),
    url(r'^order/$', views.order, name='order')
]