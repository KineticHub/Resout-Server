#resout/resout_app
from django.contrib import admin
from resout_app.models import *

admin.site.register(Reservation)
admin.site.register(ReservationAdminUser)