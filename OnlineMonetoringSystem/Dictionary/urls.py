from django.conf.urls import url,include
from . import views
from Dictionary.views import *

urlpatterns = [

    url(r'^$',register_action,name="register_action"),
    url(r'^activity/$',register_activity,name="register_activity"),
    url(r'^action/(?P<id>\d+)/delete/$',delete_action,name='delete_action'),
    url(r'^activity/(?P<id>\d+)/delete/$',delete_activity,name='delete_activity'),

]
