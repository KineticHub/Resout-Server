#resout/reservations_app
from django.contrib import admin
from resout_app.models import *
from reservations_app.models import *

# # ===================================================#
class FilterUserAdmin(admin.ModelAdmin):

	def save_model(self, request, obj, form, change):
		try:
			obj.user
		except:
			obj.user = request.user

			if not request.user.is_superuser:
				try:
					res_admin = ReservationAdminUser.objects.get(pk=request.user.id)
					obj.reservation = res_admin.reservation
				except:
					# THIS SHOULD NOT HAPPEN, BUT SMOOTH HANDING IS GOOD
					pass

		obj.save()

	def get_readonly_fields(self, request, obj=None):
				if not request.user.is_superuser:
						return self.readonly_fields + ('reservation',)
				return self.readonly_fields

	def queryset(self, request): 
		qs = super(FilterUserAdmin, self).queryset(request)
		if request.user.is_superuser:
					return qs
				res_admin = ReservationAdminUser.objects.get(pk=request.user.id)
		return qs.filter(reservation=res_admin.reservation)

	# def has_change_permission(self, request, obj=None):
		# if not obj:
			# # the changelist itself
			# return True
		# if request.user.is_superuser:
						# return True
		# return obj.user == request.user

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == "type" and not request.user.is_superuser:
								res_admin = ReservationAdminUser.objects.get(pk=request.user.id)
				kwargs["queryset"] = ReservationDocumentType.objects.filter(reservation=res_admin.reservation)
				return db_field.formfield(**kwargs)
		# if db_field.name == "bar" and not request.user.is_superuser:
				# kwargs["queryset"] = VenueBar.objects.filter(user=request.user)
				# return db_field.formfield(**kwargs)
		# if db_field.name == "drink_type" and not request.user.is_superuser:
				# kwargs["queryset"] = DrinkType.objects.filter(user=request.user)
				# return db_field.formfield(**kwargs)
		return super(FilterUserAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
# # ===================================================#

# class ReservationSiteAdministratorAdmin(FilterUserAdmin):
	# exclude = ('user', 'reservation')

class ReservationCampAdmin(FilterUserAdmin):
	exclude = ('user',)
	
	def queryset(self, request): 
		qs = super(FilterUserAdmin, self).queryset(request)
		if request.user.is_superuser:
					return qs
		if not request.user.is_superuser:
					try:
						res_admin = ReservationAdminUser.objects.get(pk=request.user.id)
						return qs.filter(reservation=res_admin.reservation)
					except:
						try:
							camp_admin = CampAdminUser.objects.get(pk=request.user.id)
							return qs.get(pk=camp_admin.camp.pk)
						except:
							# THIS SHOULD NOT HAPPEN, BUT SMOOTH HANDLING IS GOOD
							pass
	
class ReservationDocumentTypeAdmin(FilterUserAdmin):
	exclude = ('user',)
	
class ReservationDocumentAdmin(FilterUserAdmin):
	exclude = ('user',)
	
class ReservationContactAdmin(FilterUserAdmin):
	exclude = ('user',)

#admin.site.register(ReservationSiteAdministrator)
admin.site.register(ReservationCamp, ReservationCampAdmin)
admin.site.register(ReservationDocumentType, ReservationDocumentTypeAdmin)
admin.site.register(ReservationDocument, ReservationDocumentAdmin)
admin.site.register(ReservationContact, ReservationContactAdmin)
