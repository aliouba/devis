from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from presta_viticoles.views import *
from rest_framework import routers


urlpatterns = patterns('',
    url(r'^api/company/(?P<siret>[0-9]+)/$', CompanyDetail.as_view()),
    url(r'^api/conf/(?P<siret>[0-9]+)/$', ConfDetail.as_view()),
    url(r'^api/group_activities/(?P<siret>[0-9]+)/$', ActivitiesGroupList.as_view()),
    url(r'^api/estimates_customer/(?P<customerID>[0-9]+)/$', EstimatesCustomerList.as_view()),
    url(r'^api/Cbenefits/(?P<customerID>[0-9]+)/$',EstimatesCustomerList.as_view()),
    url(r'^api/CbenefitsList/(?P<customerID>[0-9]+)/$',CEstimatesList.as_view()),
    url(r'^make_estimate/(?P<siret>[0-9]+)/$', make_estimate),
    url(r'^Clogin$',login_customer, name='Clogin'),
    url(r'^Cbenefits/(?P<customerID>[0-9]+)/$',CEstimatesView.as_view(), name='estimates_for_customer'),
    #url(r'^Ebenefits/(?P<siret>[0-9]+)/$',Ebenefits, name='benefits_for_companies'),
)
