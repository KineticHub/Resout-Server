#resout/resout_app
from django.contrib import admin
from resout_app.models import *

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = ReservationAdminUser2

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
	fields = ('username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'is_reservation_admin2')

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('is_reservation_admin2',)}),
    )


admin.site.register(ReservationAdminUser2, MyUserAdmin)

# class CustomUserAdmin(admin.ModelAdmin):
	# list_display = ('first_name', 'last_name', 'password', 'is_reservation_admin2')
# admin.site.register(ReservationAdminUser2, CustomUserAdmin)

admin.site.register(Reservation)
admin.site.register(ReservationAdminUser)