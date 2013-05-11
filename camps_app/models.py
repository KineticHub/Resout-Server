# resout/camps_app
from django.db import models
from api_app.models import BaseModel
from reservations_app.models import ReservationCamp
from meritbadges_app.models import MeritBadge

class CampDocument(BaseModel):

	DOC_FORMATS = (('IMAGE', 'IMAGE'), ('PDF','PDF'))
        
	camp = models.ForeignKey(ReservationCamp)
	name = models.CharField(max_length=255)
	link = models.URLField(help_text="Please provide a URL for the document.")
	type = models.ForeignKey('CampDocumentType')
	format = models.CharField(max_length=255, choices=DOC_FORMATS)
	
	def __unicode__(self):
		return self.camp.name + " " + self.name

	class Meta:
		ordering = ['camp__name', 'name']
		
class CampDocumentType(BaseModel):

	camp = models.ForeignKey(ReservationCamp)
	name = models.CharField(max_length=255)
		
	def __unicode__(self):
		return self.name
		
	class Meta:
		ordering = ['name']

class CampContact(BaseModel):
	camp = models.ForeignKey(ReservationCamp)
	name = models.CharField(max_length=255)
	number = models.CharField(max_length=15, blank = True, help_text="Please use digits only, i.e. 8881112222.")
	email = models.EmailField(blank = True)
	position = models.CharField(max_length=255)

	def __unicode__(self):
		return self.camp.name + " " + self.name

	class Meta:
		ordering = ['camp__name', 'name']
		
class CampArea(BaseModel):
	camp = models.ForeignKey(ReservationCamp)
	name = models.CharField(max_length=255)
	image = models.URLField(blank = True, help_text="Please provide a URL for the image.")
	schedule = models.ForeignKey(CampDocument, blank=True, null=True)
	description = models.TextField(blank=True)

	def __unicode__(self):
		return self.camp.name + " " + self.name

	class Meta:
		ordering = ['camp__name', 'name']

class CampRank(BaseModel):
	camp = models.ForeignKey(ReservationCamp)
	name = models.CharField(max_length=255)
	order = models.IntegerField(help_text="A number representing the rank hierarchy, with lower numbers being higher in rank.")

	def __unicode__(self):
		return self.camp.name + " " + self.name
	
	class Meta:
		ordering = ['camp__name', 'order', 'name']

class CampStaff(BaseModel):
	camp = models.ForeignKey(ReservationCamp)
	name = models.CharField(max_length=255)
	area = models.ForeignKey(CampArea)
	rank = models.ForeignKey(CampRank)
	thumbnail = models.URLField(blank = True, help_text="Please provide a URL for the image.")

	def __unicode__(self):
		return self.camp.name + " " + self.name

	class Meta:
		ordering = ['camp__name', 'name']
		
class CampMeritBadge(BaseModel):
	camp = models.ForeignKey(ReservationCamp)
	badge = models.ForeignKey(MeritBadge)
	area = models.ForeignKey(CampArea)
		
	def __unicode__(self):
		return self.camp.name + " " + self.badge.name
		
	class Meta:
		ordering = ['camp__name', 'badge__name']
