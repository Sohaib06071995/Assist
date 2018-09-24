from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import login, logout
from UserAccount.views import *

urlpatterns = [

    url(r'^$',Login,name='Login'),
    # we are getting the login already made and passing to login.html
    url(r'^login/$',login, {'template_name': 'UserAccount/login.html'}),
    url(r'^logout/$',logout, {'template_name': 'UserAccount/logout.html'}),
    url(r'^cp/$',control_panel),
    url(r'^cp/register/$',register_user,name='register_user'),
    url(r'^cp/(?P<username>[\w.@+-]+)/(?P<id>\d+)/update/$',update_user,name='update_user'),
    url(r'^cp/(?P<id>\d+)/(?P<username>[\w.@+-]+)/delete/$',delete_user,name='delete_user'),
    

]
