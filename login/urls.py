from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.acc_login,name='login'),
    url(r'^login/$',views.acc_login,name='login'),
    url(r'^logout/$',views.acc_logout),
    url(r'^index/$',views.index),
    url(r'^userlist/$',views.UserListView.as_view()),
    url(r'^userlist/(?P<pk>\d+)/$',views.UserDetailView.as_view()),

]