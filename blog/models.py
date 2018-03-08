from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField(default=timezone.now)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
