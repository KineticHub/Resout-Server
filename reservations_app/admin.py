#resout/reservations_app
from django.contrib import admin
from reservations_app.models import *

admin.site.register(ReservationSiteAdministrators)
admin.site.register(ReservationCamp)
admin.site.register(ReservationDocumentType)
admin.site.register(ReservationDocument)
admin.site.register(ReservationContact)