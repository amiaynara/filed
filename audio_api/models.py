from django.db import models
from djnago.utils import timezone
# Create your models here.

class Song(models.Model):
    name        = models.TextField(max_length=100)
    duration    = models.IntegerField()
    upload_time = models.DateTimeField(default=timezone.now)    # We can define time zone in settings.py

class Podcast(models.Model):
    name        = models.TextField(max_length=100)
    duration    = models.IntegerField()
    upload_time = models.DateTimeField(default=timezone.now)
    host        = models.CharField(max_length=100, blank=True, null=True)
    #participts = models.ArrayField()

class AudioBook(models.Model):
    title       = models.CharField(max_length=100)
    author      = models.CharField(max_length=100)
    narrator    = models.CharField(max_length=100)
    duration    = models.IntegerField()
    upload_time = models.DateTimeField(default=timezone.now)


