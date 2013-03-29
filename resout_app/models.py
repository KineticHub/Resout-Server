# resout/resout_app
from django.db import models
from django.contrib.auth.models import User
from api_app.models import BaseModel

class Reservation(BaseModel):
	reservation_director = models.ForeignKey(User, related_name='reservation_director')
	name = models.CharField(max_length=255)
	contact_email = models.EmailField(max_length=255, blank=True)
	contact_number = models.PositiveIntegerField(blank=True, null=True)
	address = models.TextField()
	image = models.URLField(blank=True)
	facebook_id = models.CharField(max_length=255, blank=True, null=True)
	#foursquare_id = models.CharField(max_length=255, blank=True, null=True)
	latitude = models.FloatField(blank=True, null=True)
	longitude = models.FloatField(blank=True, null=True)
