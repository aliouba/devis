from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from presta_viticoles.views import *
from presta_viticoles.viewsapi import *
from rest_framework import routers


urlpatterns = patterns('',
    url(r'^api/company/(?P<siret>[0-9]+)/$', CompanyDetail.as_view()),
    url(r'^api/conf/(?P<siret>[0-9]+)/$', ConfDetail.as_view()),
    url(r'^api/group_activities/(?P<siret>[0-9]+)/$', ActivitiesGroupList.as_view()),
    url(r'^api/Cbenefits/(?P<customerID>[0-9]+)/$',EstimatesCustomerList.as_view()),  
    url(r'^make_estimate/(?P<siret>[0-9]+)/$', make_estimate),
    url(r'^Clogin/$',login_customer, name='Clogin'),
    url(r'^CloginAjax/$',login_customerAJAX, name='CloginAjax'),
    url(r'^Clogout/$',logout_customer, name='Clogout'),
    url(r'^Cbenefits/(?P<customerID>[0-9]+)/$',estimates_customer, name='estimates_for_customer'),
)
