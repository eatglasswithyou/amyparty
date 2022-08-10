from django.db import models

# Create your models here.

class Attendee(models.Model):
	title = models.CharField(max_length=100, blank=False)
	email = models.EmailField(max_length=100, blank=False)
	size = models.IntegerField(blank=False)
	rsvp = models.CharField(max_length=20, blank=False)
	consent = models.CharField(max_length=20)