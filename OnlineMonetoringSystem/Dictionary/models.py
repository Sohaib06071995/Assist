from django.db import models

# Create your models here.
class Action(models.Model):
    Actions = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.Actions



class Activity(models.Model):
    Activities = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.Activities
