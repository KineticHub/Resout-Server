#resout/camps_app
from django.contrib import admin
from django.contrib.auth.models import User, Group
from resout_app.models import *
from camps_app.models import *

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
                        obj.camp.reservation = res_admin.reservation
                    except:
                        try:
                            camp_admin = CampAdminUser.objects.get(pk=request.user.id)
                            obj.camp = camp_admin.camp
                            obj.camp.reservation = camp_admin.reservation
                        except:
                            # THIS SHOULD NOT HAPPEN, BUT SMOOTH HANDLING IS GOOD
                            pass

		obj.save()

	def get_readonly_fields(self, request, obj=None):
                if request.user.groups.filter(name='Camp Admins').exists():
                        return self.readonly_fields + ('camp',)
                return self.readonly_fields

	def queryset(self, request): 
		qs = super(FilterUserAdmin, self).queryset(request)
		if request.user.is_superuser:
                    return qs
                try:
                    res_admin = ReservationAdminUser.objects.get(pk=request.user.id)
                    return qs.filter(camp.reservation=res_admin.reservation)
                except:
                    try:
                        camp_admin = CampAdminUser.objects.get(pk=request.user.id)
                        return qs.filter(camp=camp_admin.camp)
                    except:
                        # THIS SHOULD NOT HAPPEN, BUT SMOOTH HANDING IS GOOD
                        pass
		return None

	# def has_change_permission(self, request, obj=None):
		# if not obj:
			# # the changelist itself
			# return True
		# if request.user.is_superuser:
						# return True
		# return obj.user == request.user

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		#if db_field.name == "type" and not request.user.is_superuser:
                                #res_admin = ReservationAdminUser.objects.get(pk=request.user.id)
				#kwargs["queryset"] = ReservationDocumentType.objects.filter(reservation=res_admin.reservation)
				#return db_field.formfield(**kwargs)
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

class CampDocumentAdmin(FilterUserAdmin):
	exclude = ('user',)
	
class CampDocumentTypeAdmin(FilterUserAdmin):
	exclude = ('user',)
	
class CampAreaAdmin(FilterUserAdmin):
	exclude = ('user',)
	
class CampRankAdmin(FilterUserAdmin):
	exclude = ('user',)

class CampStaffAdmin(FilterUserAdmin):
	exclude = ('user',)

class CampContactAdmin(FilterUserAdmin):
	exclude = ('user',)

class CampMeritBadgeAdmin(FilterUserAdmin):
	exclude = ('user',)

admin.site.register(CampDocument, CampDocumentAdmin)
admin.site.register(CampDocumentType, CampDocumentTypeAdmin)
admin.site.register(CampArea, CampAreaAdmin)
admin.site.register(CampRank, CampRankAdmin)
admin.site.register(CampStaff, CampStaffAdmin)
admin.site.register(CampContact, CampContactAdmin)
admin.site.register(CampMeritBadge, CampMeritBadgeAdmin)
