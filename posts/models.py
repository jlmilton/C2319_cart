from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
CATEGORY = (
    (0,"Electronic"),
    (1,"Furniture"),
    (2,"Major Appliance"),
    (3,"Kitchen"),
    (4,"Books"),
    (5,"Motors")
)
CONDITION = {
    (0,"Brand New"),
    (1, "Used - Like New"),
    (2, "Used - Good"),
    (3, "Used - working"),
    (4, "Used - Not Working")
}

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post" , null=True)
    title = models.CharField(max_length=255)
    body = models.TextField(null=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    category = models.IntegerField(choices=CATEGORY, default=0)
    cover = models.ImageField(upload_to='images/', null=True , blank=True)
    condition = models.IntegerField(choices=CONDITION , default = 4)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00), null=True ,blank=True)
    publish = models.IntegerField(choices=STATUS, default=0)
