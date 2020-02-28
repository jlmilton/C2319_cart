from django.db import models
from django.contrib.auth.models import User
# Create your models here.

JOB = (
    (0,"Undergraduate Student"),
    (1,"Graduate Student"),
    (2,"Faculty Member"),
    (3,"Staff"),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    location = models.CharField(max_length=30)
    age = models.IntegerField()
    occupation = models.IntegerField(choices=JOB , default = 4)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)


    def __str__(self):
        return self.user.username
