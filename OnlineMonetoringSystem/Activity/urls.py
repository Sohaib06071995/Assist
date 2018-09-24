from django.conf.urls import url,include
from . import views
from Activity.views import *

urlpatterns = [
    url(r'^$',register_activitiess,name="register_activitiess"),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^register/(?P<id>\d+)/update/$',update_activitiess,name='update_activitiess'),
    url(r'^register/(?P<id>\d+)/delete/$',delete_activitiess,name='delete_activitiess'),
    url(r'^register/(?P<id>\d+)/showdashboard/$',show_dashboard,name="show_dashboard"),
    url(r'^register/(?P<id>\d+)/updatestatus/$',update_status,name='update_status'),
    url(r'^register/(?P<id>\d+)/progress/$',progress_create,name="progress_create"),
    url(r'^register/(?P<id>\d+)/updateprogressnotification/$',update_progress_notification,name='update_progress_notification'),
    url(r'^register/(?P<id>\d+)/updatecommentnotification/$',update_comment_notification,name='update_comment_notification'),


]
