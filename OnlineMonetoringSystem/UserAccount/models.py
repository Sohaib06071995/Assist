from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
USER_TYPE = [
('administration','Administration'),
('normal','Normal'),
]
class User_Account(models.Model):
    user = models.OneToOneField(User,'on_delete')

    position_title = models.CharField(max_length=100, default='')
    user_type = models.CharField(max_length=100,choices=USER_TYPE, blank=False)
    user_name = models.CharField(max_length=100,default='')
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username

# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_account = User_Account.objects.create(user=kwargs['instance'])
# post_save.connect(create_profile, sender=User)
