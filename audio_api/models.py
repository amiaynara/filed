from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Song(models.Model):
    name        = models.CharField(max_length=100)
    duration    = models.IntegerField()
    upload_time = models.DateTimeField(default=timezone.now)    # We can define time zone in settings.py

class Podcast(models.Model):
    name        = models.CharField(max_length=100)
    duration    = models.IntegerField()
    upload_time = models.DateTimeField(default=timezone.now)
    host        = models.CharField(max_length=100)
    prtcpnts    = ArrayField(models.CharField(max_length=100, blank=True, null=True), size=10, blank=True)
    options     = models.JSONField(null=True, blank=True)

class AudioBook(models.Model):
    title       = models.CharField(max_length=100)
    author      = models.CharField(max_length=100)
    narrator    = models.CharField(max_length=100)
    duration    = models.IntegerField()
    upload_time = models.DateTimeField(default=timezone.now)


