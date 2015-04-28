import json

from presta_viticoles.models import *
from presta_viticoles.serializers import *
from presta_viticoles.forms import *

from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils.six import BytesIO
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.conf.urls import url
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class CompanyDetail(APIView):
    """
    Retrieve, update or delete a company instance.
    """
    def get_object(self, siret):
        try:
            return Company.objects.get(siret=siret)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, siret, format=None):
        company = self.get_object(siret)
        serializer = CompanySerializer(company)
        return Response(serializer.data)
class ConfDetail(APIView):
    """
    Retrieve, update or delete a company instance.
    """
    def get_object(self, siret):
        try:
            company = Company.objects.filter(siret=siret)[0]
            return ConfigPrestaViticole.objects.get(company_id=company.id)
        except ConfigPrestaViticole.DoesNotExist:
            raise Http404

    def get(self, request, siret, format=None):
        conf = self.get_object(siret)
        serializer = ConfigPrestaViticoleSerializer(conf)
        return Response(serializer.data)
class ActivitiesGroupList(APIView):
    """
    List all activities, or create a new activity.
    """
    def get(self, request, siret , format=None):
        company = Company.objects.filter(siret=siret)[0]
        acts = ActivityGroup.objects.filter(activity__company=company.id).distinct()
        serializer = GroupActivitiesSerializer(acts,many=True)
        return Response(serializer.data)
class EstimatesCustomerList(APIView):
    def get(self, request, customerID , format=None):
        estim = Estimate.objects.filter(customer_id=customerID)
        serializer = EstimateSerializer(estim,many=True)
        return Response(serializer.data)
class CEstimatesList(APIView):
    """
    List of all estimates by customer.
    """
    def get(self, request, customerID , format=None):
        cestimates= Estimate.objects.filter(customer=customerID).values('id','nb','price_with_tax','price_without_tax')
        for estimate in cestimates:
            estimate["benefits"] = Benefit.objects.filter(estimate_id=estimate["id"]).values("price_with_tax")
        print(cestimates)
        serializer = CEstimateSerializer(cestimates,many=True)
        print(serializer)
        return Response(serializer.data)
        
class CEstimatesView(ListView):
    model = Estimate 
    context_object_name = 'cestimates'
    template_name = 'presta_viticoles/home-customers.html'
    def get_context_data(self, **kwargs):
        context = super(CEstimatesView, self).get_context_data(**kwargs)
        cestimates= Estimate.objects.filter(customer=self.kwargs['customerID'])
        for estimate in cestimates:
            benefits = Benefit.objects.filter(estimate=estimate)
            estimate.benefits = benefits
            onebenefit = benefits.first()
            activity = ActivityPrestaViticole.objects.get(id=onebenefit.activity_id)
            company = Company.objects.get(id=activity.company_id)
            estimate.companyname = company.name
            estimate.companyphone = company.phonenumber
            estimate.companymail = company.mail
        context["cestimates"] = cestimates
        return context

