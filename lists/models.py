from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL



class Element(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=255)
    checked = models.BooleanField(default=False)

class List(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    visibility = models.CharField(max_length=255)
    hashtags = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    elements = models.ManyToManyField(Element)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)