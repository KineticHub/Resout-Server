#resout/resout_app
from django.contrib import admin
from resout_app.models import *

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

class CampAdminUserChangeForm(UserChangeForm):
	class Meta:#(UserChangeForm.Meta):
		model = CampAdminUser
		#fields = ('username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'is_reservation_admin2')
		
class ReservationAdminUserChangeForm(UserChangeForm):
	class Meta:#(UserChangeForm.Meta):
		model = ReservationAdminUser
		#fields = ('username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'is_reservation_admin2')
		

class CampAdminUserAdmin(UserAdmin):
	form = CampAdminUserChangeForm
	#fields = ('username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'is_reservation_admin2')
	#exclude = ('is_superuser',)

	#fieldsets = UserAdmin.fieldsets + (
		#(None, {'fields': ('is_reservation_admin2',)}),
	#)
	
	fieldsets = (
		(None, {'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'camp')}),
	)
	
	def save_model(self, request, obj, form, change):
		
		if not request.user.is_superuser:
			try:
				res_admin = ReservationAdminUser.objects.get(pk=request.user.id)
				obj.reservation = res_admin.reservation
			except:
				pass
		obj.save()
	
class ReservationAdminUserAdmin(UserAdmin):
	form = ReservationAdminUserChangeForm
	#fields = ('username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'is_reservation_admin2')
	#exclude = ('is_superuser',)

	#fieldsets = UserAdmin.fieldsets + (
		#(None, {'fields': ('is_reservation_admin2',)}),
	#)
	
	fieldsets = (
		(None, {'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'reservation')}),
	)

	def save_model(self, request, obj, form, change):
		
		if not request.user.is_superuser:
			try:
				res_admin = ReservationAdminUser.objects.get(pk=request.user.id)
				obj.reservation = res_admin.reservation
			except:
				pass
		obj.save()

#admin.site.register(ReservationAdminUser2, MyUserAdmin)

# class CustomUserAdmin(admin.ModelAdmin):
	# list_display = ('first_name', 'last_name', 'password', 'is_reservation_admin2')
# admin.site.register(ReservationAdminUser2, CustomUserAdmin)

admin.site.register(Reservation)
admin.site.register(ReservationAdminUser, ReservationAdminUserAdmin)
admin.site.register(CampAdminUser, CampAdminUserAdmin)