from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('ResOut',

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('ApiApp.views',

	#url(r'^api/token/$', 'EmptyTokenCall'),

	url(r'^api/reservation/camps/(?P<res_id>\d{1,10})/$', 'ReservationCamps'),
	url(r'^api/reservation/documents/(?P<res_id>\d{1,10})/$', 'ReservationDocuments'),
	url(r'^api/reservation/contacts/(?P<res_id>\d{1,10})/$', 'ReservationContacts'),

	url(r'^api/camp/areas/(?P<camp_id>\d{1,10})/$', 'CampAreas'),
	url(r'^api/camp/contacts/(?P<camp_id>\d{1,10})/$', 'CampContacts'),
	url(r'^api/camp/documents/(?P<camp_id>\d{1,10})/$', 'CampDocuments'),
	url(r'^api/camp/ranks/(?P<camp_id>\d{1,10})/$', 'CampRanks'),
        url(r'^api/camp/staff/(?P<camp_id>\d{1,10})/$', 'CampStaff'),
)

urlpatterns += patterns('',
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/admin/'}),
    (r'^grappelli/', include('grappelli.urls')),
)
