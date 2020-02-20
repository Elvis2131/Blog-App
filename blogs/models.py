from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50, null = False, blank = False)
    summary = models.CharField(max_length=100)
    description = models.TextField(max_length=250, null = False)
    active = models.BooleanField(default=False)