#resout/meritbadges_app
from django.contrib import admin
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from nested_inlines.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline

from meritbadges_app.models import *

class SubRequirement_Lvl2Form():

	class Meta:
		model = SubRequirement_Lvl2
		
class SubRequirement_Lvl2Inline(NestedStackedInline):
	model =  SubRequirement_Lvl2
	extra = 0
	#form = SubRequirement_Lvl2Form

class SubRequirement_Lvl1Form(ModelForm):
	#def __init__(self, *args, **kwargs):
		#super(DrinkOrderedForm, self).__init__(*args, **kwargs)
		#self.fields['drink_name'] = forms.ModelChoiceField(queryset=Drink.objects.all())
		
	inlines = [SubRequirement_Lvl2Inline,]

	class Meta:
		model = SubRequirement_Lvl1

class SubRequirement_Lvl1Inline(NestedStackedInline):
	model =  SubRequirement_Lvl1
	extra = 0
	inlines = [SubRequirement_Lvl2Inline,]
	#form = SubRequirement_Lvl1Form

class RequirementModelAdmin(NestedModelAdmin):
	#exclude = ('user',)
	inlines = [SubRequirement_Lvl1Inline,]

admin.site.register(MeritBadge)
admin.site.register(Requirement, RequirementModelAdmin)
#admin.site.register(SubRequirement_Lvl1)
#admin.site.register(SubRequirement_Lvl2)
admin.site.register(SubRequirement_Lvl3)
