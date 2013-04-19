#resout/resout_app
from django.contrib import admin
from resout_app.models import *

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

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
	
	restricted_fieldsets = (
		(None, {'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'is_active')}),
	)
	
	# def get_form(self, request, obj=None, **kwargs):
		# self.exclude = []	
		# if not request.user.is_superuser:
			# self.exclude.append('reservation')
		# return super(CampAdminUserAdmin, self).get_form(request, obj, **kwargs)
		
	def queryset(self, request):
		if request.user.is_superuser:
			return User.objects.all()
			
		res_admin = ReservationAdminUser.objects.get(pk=request.user.id)
		return CampAdminUserAdmin.objects.filter(reservation = res_admin.reservation)
		
	def get_fieldsets(self, request, obj=None):
		if request.user.is_superuser:
			return super(UserAdmin, self).get_fieldsets(request, obj)
		return self.restricted_fieldsets
	
	def save_model(self, request, obj, form, change):
		if not request.user.is_superuser:
			try:
				res_admin = ReservationAdminUser.objects.get(pk=request.user.id)
				obj.reservation = res_admin.reservation
			except:
				obj.is_active = False
		obj.is_staff = True
		obj.save()
	
class ReservationAdminUserAdmin(UserAdmin):
        temp_res = Reservation.objects.get(pk=1)
	form = ReservationAdminUserChangeForm(initial={'reservation': temp_res})
	#fields = ('username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'is_reservation_admin2')
	#exclude = ('is_superuser',)

	# fieldsets = UserAdmin.fieldsets + (
		# (None, {'fields': ('reservation',)}),
	# )

	add_fieldsets = (
                     (None, {
                          'classes': ('wide',),
                          'fields': ('username', 'email', 'password1', 'password2')}
                          ),
                         )

	add_form = UserCreationForm
	
	fieldsets = (
		(None, {'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'reservation')}),
	)
	
	restricted_fieldsets = (
		(None, {'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'is_active')}),
	)
	
	def queryset(self, request):
		if request.user.is_superuser:
			return ReservationAdminUser.objects.all()
		res_admin = ReservationAdminUser.objects.get(pk=request.user.id)
		return ReservationAdminUser.objects.filter(reservation = res_admin.reservation)

	def get_fieldsets(self, request, obj=None):
                if obj:
                        if request.user.is_superuser:
                                return self.fieldsets
                        return self.restricted_fieldsets
                else:
                        return self.add_fieldsets
	
	# def get_fieldsets(self, request, obj=None):
		# if request.user.is_superuser:
			# return self.fieldsets
		# return self.restricted_fieldsets
	
#	def get_form(self, request, obj=None, **kwargs):
#		self.exclude = []
		# if not request.user.is_superuser:
			# self.exclude.append('reservation')
#		return super(UserAdmin, self).get_form(request, obj, **kwargs)

	def save_model(self, request, obj, form, change):
		#if not request.user.is_superuser:
			#try:
				res_admin = ReservationAdminUser.objects.get(pk=request.user.id)
				obj.reservation = res_admin.reservation
			#except:
				#obj.is_active = False
                                obj.is_staff = True
                                obj.save()

#admin.site.register(ReservationAdminUser2, MyUserAdmin)

# class CustomUserAdmin(admin.ModelAdmin):
	# list_display = ('first_name', 'last_name', 'password', 'is_reservation_admin2')
# admin.site.register(ReservationAdminUser2, CustomUserAdmin)

admin.site.unregister(User)
admin.site.register(Reservation)
admin.site.register(ReservationAdminUser, ReservationAdminUserAdmin)
admin.site.register(CampAdminUser, CampAdminUserAdmin)
