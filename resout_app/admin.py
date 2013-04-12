#resout/resout_app
from django.contrib import admin
from resout_app.models import *

class CustomUserAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'password', 'is_reservation_admin2')
admin.site.register(ReservationAdminUser2, CustomUserAdmin)

admin.site.register(Reservation)
admin.site.register(ReservationAdminUser)