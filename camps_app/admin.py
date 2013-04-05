#resout/camps_app
from django.contrib import admin
from camps_app.models import *

admin.site.register(CampDocument)
admin.site.register(CampDocumentType)
admin.site.register(CampArea)
admin.site.register(CampRank)
admin.site.register(CampStaff)
admin.site.register(CampContact)
admin.site.register(CampMeritBadge)
