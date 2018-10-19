from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^erp/$', views.erp, name='erp_export'),
]