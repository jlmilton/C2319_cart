from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify # new


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(null=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
