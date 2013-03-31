#resout/reservations_app
from django.db import models
from django.contrib.auth.models import User
from api_app.models import BaseModel
from resout_app.models import Reservation

class ReservationSiteAdministrator(BaseModel):
	reservation = models.ForeignKey(Reservation)
	res_site_admin = models.OneToOneField(User, related_name='res_site_admin')
	is_ReservationAdmin = models.BooleanField(default=False)
	is_CampAdmin = models.BooleanField(default=False) 

class ReservationCamp(BaseModel):

	reservation = models.ForeignKey(Reservation)
	name = models.CharField(max_length=255)
	image = models.URLField()
	description = models.TextField()
	
	def __unicode__(self):
		return self.name
		
class ReservationDocumentType(BaseModel):

	reservation = models.ForeignKey(Reservation)
	name = models.CharField(max_length=255)
		
	def __unicode__(self):
		return self.name
		
	class Meta:
		ordering = ['name']
		
class ReservationDocument(BaseModel):
        
	DOC_FORMATS = (('IMAGE', 'IMAGE'), ('PDF','PDF'))
	
	
	reservation = models.ForeignKey(Reservation)
	name = models.CharField(max_length=255)
	link = models.URLField()
	type = models.ForeignKey(ReservationDocumentType)
	format = models.CharField(max_length=255, choices=DOC_FORMATS)
	
	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']
	
class ReservationContact(BaseModel):

	reservation = models.ForeignKey(Reservation)
	name = models.CharField(max_length=255)
	number = models.CharField(max_length=15, blank = True)
	email = models.EmailField(blank = True)
	position = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name
