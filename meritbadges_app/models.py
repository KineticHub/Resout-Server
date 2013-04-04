# resout/meritbadges_app
from django.db import models
from api_app.models import BaseModel

class MeritBadge(BaseModel):
	name = models.CharField(max_length=100, unique=True)
	thumbnail = models.URLField(blank=True)
	
	class Meta:
		ordering = ['name']
	
	def __unicode__(self):
		return self.name

class Requirement(BaseModel):
	badge = models.ForeignKey(MeritBadge, related_name = 'requirements')
	requirement_number = models.IntegerField()
	description = models.TextField()
	prerequisite = models.BooleanField()
	
	class Meta:
		ordering = ['badge', 'requirement_number']
		
	def __unicode__(self):
		return self.badge.name + ", Req " + str(self.requirement_number)
		
class SubRequirement_Lvl1(BaseModel):
	requirement = models.ForeignKey(Requirement, related_name = 'subrequirements_lvl1')
	subrequirement_letter = models.CharField(max_length=1)
	description = models.TextField()
	#prerequisite = models.BooleanField()
	
	class Meta:
		ordering = ['requirement', 'subrequirement_letter']
	
	def __unicode__(self):
		return self.requirement.badge.name + ", Req " + str(self.requirement.requirement_number) + ", SubReq " + str(self.subrequirement_letter)
		
class SubRequirement_Lvl2(BaseModel):
	subrequirement = models.ForeignKey(SubRequirement_Lvl1, related_name = 'subrequirements_lvl2')
	subrequirement_number = models.IntegerField()
	description = models.TextField()
	#prerequisite = models.BooleanField()
	
	class Meta:
		ordering = ['subrequirement', 'subrequirement_number']
	
	def __unicode__(self):
		return self.subrequirement.requirement.badge.name + ", Req " + str(self.subrequirement.requirement.requirement_number) + ", SubReq " + str(self.subrequirement.subrequirement_letter) + ", SubReq " + str(self.subrequirement_number)
		
class SubRequirement_Lvl3(BaseModel):
	subrequirement = models.ForeignKey(SubRequirement_Lvl2, related_name = 'subrequirements_lvl3')
	subrequirement_letter = models.CharField(max_length=1)
	description = models.TextField()
	#prerequisite = models.BooleanField()
	
	class Meta:
		ordering = ['subrequirement', 'subrequirement_letter']
	
	def __unicode__(self):
		return self.subrequirement.subrequirement.requirement.badge.name + ", Req " + str(self.subrequirement.subrequirement.requirement.requirement_number) + ", SubReq " + str(self.subrequirement.subrequirement.subrequirement_letter) + ", SubReq " + str(self.subrequirement.subrequirement_number) + ", SubReq " + str(self.subrequirement_letter)
