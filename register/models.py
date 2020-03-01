from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

JOB = (
    (0,"Undergraduate Student"),
    (1,"Graduate Student"),
    (2,"Faculty Member"),
    (3,"Staff"),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, default=0, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    occupation = models.IntegerField(choices=JOB , default = 4)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=150, null=False, blank=False)



    def __str__(self):
        return self.user.username

# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = UserProfile.objects.create(user = kwargs['instance'])
#
# post_save.connect(create_profile , sender=User)
