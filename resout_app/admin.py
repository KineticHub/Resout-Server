#resout/resout_app
from django.contrib import admin
from resout_app.models import *
from reservations_app.models import *

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group

class ReservationAdmin(admin.ModelAdmin):
	
	def queryset(self, request):
		qs = super(ReservationAdmin, self).queryset(request)
		if request.user.is_superuser:
                        return qs
                res_admin = ReservationAdminUser.objects.get(pk=request.user.id)
		return qs.filter(pk=res_admin.reservation.id)

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

	add_fieldsets = (
                     (None, {
                          'classes': ('wide',),
                          'fields': ('username', 'email', 'password1', 'password2')}
                          ),
                         )

	add_form = UserCreationForm
	
	fieldsets = (
		(None, {'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'reservation', 'camp')}),
	)
	
	restricted_fieldsets = (
		(None, {'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'is_active')}),
	)
	
	# def get_form(self, request, obj=None, **kwargs):
		# self.exclude = []	
		# if not request.user.is_superuser:
			# self.exclude.append('reservation')
		# return super(CampAdminUserAdmin, self).get_form(request, obj, **kwargs)
		
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
                if db_field.name == "camp" and not request.user.is_superuser:
                        res_admin = ReservationAdminUser.objects.get(pk=request.user.id)
                        kwargs["queryset"] = ReservationCamp.objects.filter(reservation=res_admin.reservation)
			return db_field.formfield(**kwargs)
		return super(CampAdminUserAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
		
		
	def get_readonly_fields(self, request, obj=None):
                if not request.user.is_superuser:
                        return self.readonly_fields + ('reservation',)
                return self.readonly_fields
	
	def queryset(self, request):
		if request.user.is_superuser:
			return CampAdminUser.objects.all()
		res_admin = ReservationAdminUser.objects.get(pk=request.user.id)
		return CampAdminUser.objects.filter(reservation = res_admin.reservation)

	def get_fieldsets(self, request, obj=None):
                if obj:
                        return self.fieldsets
                        #if request.user.is_superuser:
                                #return self.fieldsets
                        #return self.restricted_fieldsets
                else:
                        return self.add_fieldsets
	
	def save_model(self, request, obj, form, change):
		if not request.user.is_superuser:
			try:
				res_admin = ReservationAdminUser.objects.get(pk=request.user.id)
				obj.reservation = res_admin.reservation
			except:
				obj.is_active = False
		obj.is_staff = True
		obj.save()
		try:
                        group = Group.objects.get(name='Camp Admins')
                except Group.DoesNotExist:
                        # group should exist, but this is just for safety's sake, it case the improbable should happen
                        pass
                else:
                        obj.groups.add(group)
	
class ReservationAdminUserAdmin(UserAdmin):
        
	form = ReservationAdminUserChangeForm#(initial={'reservation': Reservation.objects.get(pk=1)})
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

        def get_readonly_fields(self, request, obj=None):
                if not request.user.is_superuser:
                        return self.readonly_fields + ('reservation',)
                return self.readonly_fields
	
	def queryset(self, request):
		if request.user.is_superuser:
			return ReservationAdminUser.objects.all()
		res_admin = ReservationAdminUser.objects.get(pk=request.user.id)
		return ReservationAdminUser.objects.filter(reservation = res_admin.reservation)

	def get_fieldsets(self, request, obj=None):
                if obj:
                        return self.fieldsets
                        #if request.user.is_superuser:
                                #return self.fieldsets
                        #return self.restricted_fieldsets
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
		if not request.user.is_superuser:
			try:
				res_admin = ReservationAdminUser.objects.get(pk=request.user.id)
				obj.reservation = res_admin.reservation
			except:
				obj.is_active = False
		obj.is_staff = True
                obj.save()

		try:
                        group = Group.objects.get(name='Reservation Admins')
                except Group.DoesNotExist:
                        # group should exist, but this is just for safety's sake, it case the improbable should happen
                        pass
                else:
                        obj.groups.add(group)

#admin.site.register(ReservationAdminUser2, MyUserAdmin)

# class CustomUserAdmin(admin.ModelAdmin):
	# list_display = ('first_name', 'last_name', 'password', 'is_reservation_admin2')
# admin.site.register(ReservationAdminUser2, CustomUserAdmin)

admin.site.unregister(User)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(ReservationAdminUser, ReservationAdminUserAdmin)
admin.site.register(CampAdminUser, CampAdminUserAdmin)
