from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=250)
    date_posted = models.DateTimeField()
    author = models.OneToOneField(User, on_delete=models.CASCADE)
