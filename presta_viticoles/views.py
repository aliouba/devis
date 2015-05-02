import json

from presta_viticoles.models import *
from presta_viticoles.serializers import *
from presta_viticoles.forms import *

from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.six import BytesIO
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

def make_estimate(request,siret):
    if request.method == 'POST':
        benefitsSelected = {}
        estimate = {}
        """
        Recuperation 
        du POST
        """
        data = json.loads(request.body.decode('utf-8'))
        benefits =  data['benefits']
        Userparaams = data['allparams']
        
        company = Company.objects.get(siret=siret)
        #Check USER
        user_params_checked = check_post_new_estimate(request,Userparaams,company.name)
        
        acts = ActivityGroup.objects.filter(activity__company=company.id).distinct()
        serializer = GroupActivitiesSerializer(acts,many=True)
        content = JSONRenderer().render(serializer.data)
        stream = BytesIO(content)
        groups = JSONParser().parse(stream)

        k=0
        for benefit in benefits:
            for group in groups:
                if group['id'] == benefit['group']:
                    activitiesIngroup = group['activities']
                    for activity in activitiesIngroup:
                        if activity['id'] == int(benefit['activity']):
                            new = {}
                            new['activity'] = activity['id']
                            new['name'] = activity['name']
                            new['description'] = activity['description']
                            if Userparaams['optionsguyot'] == 'gd':
                                new['unitPrice'] = activity['price_plant_gd']
                                new['tax'] = activity['tax']
                            elif Userparaams['optionsguyot'] == 'gs':
                                new['unitPrice'] = activity['price_plant_gs']
                                new['tax'] = activity['tax']
                            benefitsSelected[k]=new
                            k = k +1
        create_estimate(user_params_checked,benefitsSelected)
        
        return render(request, 'presta_viticoles/select-activities.html')
    else:
        form = UserAuthLoginForm()
        return render(request, 'presta_viticoles/select-activities.html',{'form':form})
def create_estimate(allparams,allbenefits):
    try:
        newcustomer = Customer.objects.get(user=allparams['customer'])
    except:
        newcustomer = Customer(mail=allparams['mail'],user=allparams['customer'])
        newcustomer.save()
    if allparams['plant_superficie']=="sup":
        newestimate = Estimate(company_name=allparams['company_name'],nb=allparams['nb'],customer=newcustomer,plant_superficie=allparams['plant_superficie'],type_guyot=allparams['type_guyot'],distance_entre_ceps=allparams['distance_entre_ceps'],largeur_entre_rangs=allparams['largeur_entre_rangs'],surface=allparams['surface'])
        newestimate.save()
    else:
        newestimate = Estimate(company_name=allparams['company_name'],nb=allparams['nb'],customer=newcustomer,plant_superficie=allparams['plant_superficie'],type_guyot=allparams['type_guyot'])
        newestimate.save()
    h=0.0
    price_ttc=0.0
    for key  in allbenefits:
        one_price_ttc=float(allbenefits[key]['unitPrice']) * allparams['nb']
        price_ttc =price_ttc + one_price_ttc
        one_h = float(allbenefits[key]['unitPrice']) * float(allbenefits[key]['tax']) *allparams['nb'] /100 
        h = h + one_h      
        newbenefit = Benefit(name=allbenefits[key]['name'],description=allbenefits[key]['description'],unit_price=allbenefits[key]['unitPrice'],tax=allbenefits[key]['tax'],price_with_tax=one_price_ttc,price_without_tax=one_price_ttc-one_h,activity_id=allbenefits[key]['activity'],estimate=newestimate)
        newbenefit.save()
    newestimate.price_with_tax = price_ttc
    price_ht = price_ttc - h
    newestimate.price_without_tax = price_ht
    newestimate.save()
def check_post_new_estimate(request,allparams,company_name):
    estimate = {}
    if allparams['parPlant']:
        estimate['nb'] = int(allparams['nombrePlants'])
        estimate['type_guyot'] = allparams['optionsguyot']
        estimate['plant_superficie'] = 'plt'
        estimate['company_name'] = company_name
    elif allparams['parSuperficie']:
        estimate['type_guyot'] = allparams['optionsguyot']
        estimate['nb'] = int(allparams['nombrePlants'])
        estimate['plant_superficie'] = 'sup'
        estimate['surface'] = float(allparams['optionssuperficie'])
        estimate['distance_entre_ceps'] = float(allparams['optionsdistceps'])
        estimate['largeur_entre_rangs'] = float(allparams['optionsdistrangs'])
        estimate['company_name'] = company_name
    if request.user.is_authenticated():
        estimate['customer'] = request.user
        estimate['mail'] = request.user.email
    else:
        try:
            user = User.objects.get(email=allparams['mail'])
            estimate['customer'] = user
            estimate['mail'] = user.email
        except:
            new_password = User.objects.make_random_password()
            user = User.objects.create_user(allparams['mail'],allparams['mail'],new_password)
            estimate['customer'] = user 
            estimate['mail'] = allparams['mail']
    return estimate
@login_required(login_url='/prestaviticoles/Clogin/')
def estimates_customer(request,customerID):
    if request.user.is_authenticated():
        try:
            customer = Customer.objects.get(id=customerID)
            if customer.user == request.user:
                return render(request, 'presta_viticoles/home-customers.html')
            else:
                return HttpResponseRedirect("/")
        except:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")
def logout_customer(request):
    logout(request)
    return HttpResponseRedirect("/")

def login_customer(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)           
        error = ""
        if user is not None:
            try:
                customer = Customer.objects.get(user=user)
            except ObjectDoesNotExist:
                return HttpResponseRedirect("Forbidden")  
            if customer.user_id == user.id and user.is_active:
                login(request, user)
                return HttpResponseRedirect("/prestaviticoles/Cbenefits/"+str(customer.id))  
            else:
                return HttpResponseRedirect("/forbidden")
        else:
            form = UserAuthLoginForm()
            return render(request, 'presta_viticoles/login.html',{'form':form}) 
    else:
        form = UserAuthLoginForm() 
        return render(request, 'presta_viticoles/login.html',{'form':form})       
