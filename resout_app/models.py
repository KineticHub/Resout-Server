# resout/resout_app
from django.db import models
from django.contrib.auth.models import User, UserManager
from api_app.models import BaseModel
#from reservations_app.models import  ReservationCamp
from geopy import geocoders

class Reservation(models.Model):
	#reservation_director = models.ForeignKey(User, related_name='reservation_director')
	#reservation_director = models.OneToOneField('ReservationAdminUser')
	name = models.CharField(max_length=255)
	contact_email = models.EmailField(max_length=255, blank=True)
	contact_number = models.PositiveIntegerField(blank=True, null=True)
	address = models.TextField()
	image = models.URLField(blank=True)
	description = models.TextField(blank=True)
	facebook_id = models.CharField(max_length=255, blank=True, null=True)
	twitter_id = models.CharField(max_length=255, blank=True, null=True)
	#foursquare_id = models.CharField(max_length=255, blank=True, null=True)
	latitude = models.FloatField(blank=True, null=True)
	longitude = models.FloatField(blank=True, null=True)
	
	def __unicode__(self):
		return self.name
		
	def save(self, *args, **kwargs):
		if not self.pk or not self.latitude or not self.longitude:
			self.set_coords()
		super(Reservation, self).save(*args, **kwargs)

        # set coordinates
        def set_coords(self):
            toFind = self.address
            g = geocoders.GoogleV3()

            place, (lat, lng) = g.geocode(toFind)

            self.latitude = lat
            self.longitude = lng

class ReservationAdminUser(User):
	reservation = models.ForeignKey(Reservation, null=True)
	
	# Use UserManager to get the create_user method, etc.
	objects = UserManager()
	
	class Meta:
		verbose_name = "Reservation Admin User"

class CampAdminUser(User):
	reservation = models.ForeignKey(Reservation, null=True)
	camp = models.ForeignKey('reservations_app.ReservationCamp', null=True)
	
	# Use UserManager to get the create_user method, etc.
	objects = UserManager()
	
	class Meta:
		verbose_name = "Camp Admin User"
	
# class CampAdminUser(AbstractUser):
	# camp = models.ForeignKey(ReservationCamp)
	# is_camp_admin = models.BooleanField(default=False) 
