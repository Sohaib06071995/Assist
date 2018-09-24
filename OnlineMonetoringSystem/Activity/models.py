from django.db import models
from UserAccount.models import *
from Dictionary.models import *
from datetime import date
from django.contrib.auth.models import User
import select2.fields
import select2.models
from django.db.models import Q
from django.core.validators import MaxValueValidator,MinValueValidator
from datetime import datetime


ACTIVITY_TYPE = [
('pending','Pending'),
('ongoing','Ongoing'),
('completed','Completed'),
('submitted','Submitted'),
]
class Pending_Activity(models.Model):
    Active_Description = models.CharField(max_length=100, default='')
    Assigned_To = select2.fields.ManyToManyField(User,
        ajax=True,
        search_field='username',
        overlay="Chose Staff...",
        js_options={
            'quiet_millis': 200,
        },

        )
    Activity_Type = models.ForeignKey(Activity,'on_delete',default='',null=True)
    Exceting_Agency = models.CharField(max_length=100,default='')
    Action_Required = models.ForeignKey(Action,'on_delete',default='',null=True)
    Assigned_Date = models.DateField(blank=True, null=True)
    Deadline = models.DateField(blank=True, null=True)
    Associated_with = models.CharField(max_length=100, default='')
    Status = models.CharField(max_length=100,default='')
    Assigned_By = models.CharField(max_length=100,null=True, default='')
    Progress = models.IntegerField(default=0,validators=[MaxValueValidator(100),MinValueValidator(0)])
    progress_by = models.ForeignKey(User,'on_delete',default='',null=True,related_name='progress_by')
    Progress_Date = models.DateField(blank=True, null=True)
    progress_notification = models.IntegerField(default=0)
    progress_notification_by = models.CharField(max_length=100,default='',null=True,)



class Comments_Activity(models.Model):
    to = models.IntegerField(null=True)
    comment = models.CharField(max_length=512,null=True, default='')
    commented_by = models.CharField(max_length=100,null=True, default='')
    commented_for = models.CharField(max_length=100,null=True, default='')
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)
    comment_notification = models.IntegerField(default=0)
    comment_notification_by = models.CharField(max_length=100,default='',null=True,)

# class Progress_Activity(models.Model):
#     to = models.IntegerField(null=True)
#     Progress = models.IntegerField(null=True)
#     Progress_Date = models.DateField(blank=True, null=True)
