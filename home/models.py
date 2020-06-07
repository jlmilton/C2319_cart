from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from posts.models import CATEGORY
from posts.models import LABEL
from posts.models import CONDITION


# Create your models here.

class About(models.Model):
    about_title = models.CharField(max_length=200)
    about_content = models.TextField()

    def __str__(self):
        return self.about_title


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY, default=0, max_length =100)
    item_label = models.CharField(choices=LABEL, default=0, max_length =100)
    condition = models.IntegerField(choices=CONDITION, default=4)
    decsription = models.TextField()

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("home:product", kwargs={"pk": self.pk})  # see how it passes arguments

    def get_add_to_cart_url(self):
        return reverse("home:add-to-cart", kwargs={"pk": self.pk})


    def get_remove_from_cart_url(self):
        return reverse("home:remove-from-cart",kwargs={"pk": self.pk})

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    ordered = models.BooleanField(default = False)
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.item_name}"

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.DateTimeField()

    def __str__(self):
        return self.user.user_name

