from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'devis.views.home', name='home'),
    url(r'^prestaviticoles/', include('presta_viticoles.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
