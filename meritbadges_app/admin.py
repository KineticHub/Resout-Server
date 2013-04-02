#resout/meritbadges_app
from django.contrib import admin
from meritbadges_app.models import *

admin.site.register(MeritBadge)
admin.site.register(Requirement)
admin.site.register(SubRequirement_Lvl1)
admin.site.register(SubRequirement_Lvl2)
admin.site.register(SubRequirement_Lvl3)