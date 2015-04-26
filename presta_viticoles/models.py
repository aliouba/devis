from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=45,null=True)
    description = models.CharField(max_length=255,null=True, blank=True)
    siret = models.CharField(max_length=14,null=True, blank=True)
    phonenumber = models.CharField(max_length=45, null=True, blank=True)
    mail = models.CharField(max_length=45, null=True, blank=True)
    cp = models.CharField(max_length=45, null=True, blank=True)
    city = models.CharField(max_length=45, null=True, blank=True)
    adresse = models.CharField(max_length=45,null=True, blank=True)
    country = models.CharField(max_length=45,null=True, blank=True)
    logo = models.FileField(max_length=45,null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    modificationdate = models.DateTimeField(null=True)
    def __str__(self):
        return u"%s" % self.name


class Employee(models.Model):
    firstname = models.CharField(max_length=45,null=True)
    lastname = models.CharField(max_length=45,null=True)
    phonenumber = models.CharField(max_length=45,null=True)
    mail = models.CharField(max_length=45,null=True)
    creationdate = models.DateTimeField(null=True)
    modificationdate = models.DateTimeField(null=True)
    company = models.ForeignKey(Company)
    user = models.ForeignKey(User)
    def __str__(self):
        return u"%s %s" % (self.firstname,self.lastname)

class ConfigPrestaViticole(models.Model):
    guyots = models.BooleanField(default=False)
    guyotd = models.BooleanField(default=False)
    superficie = models.BooleanField(default=False)
    plant = models.BooleanField(default=False)
    nb_plants_min = models.IntegerField(default=0)
    creationdate = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    modificationdate = models.DateTimeField(null=True)
    company = models.ForeignKey(Company)
    def __str__(self):
        return u"Config Of  %s" % self.company

class ActivityGroup(models.Model):
    name = models.CharField(max_length=45,null=True)
    def __str__(self):
        return u"%s" % self.name

class ActivityPrestaViticole(models.Model):
    group = models.ForeignKey(ActivityGroup, related_name='activities', related_query_name='activity')
    name = models.CharField(max_length=255,null=True)
    description = models.CharField(max_length=255,null=True)
    price_plant_gd = models.DecimalField(max_digits=10, decimal_places=3,null=True)
    price_plant_gs = models.DecimalField(max_digits=10, decimal_places=3,null=True)
    price_ha_gs = models.DecimalField(max_digits=10, decimal_places=3,null=True)
    price_ha_gd = models.DecimalField(max_digits=10, decimal_places=3,null=True)
    tax = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True,default=0)
    creationdate = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    modificationdate = models.DateTimeField(null=True)
    company = models.ForeignKey(Company)
    def __str__(self):
        return u"%s" % self.description

class Customer(models.Model):
    firstname = models.CharField(max_length=45,null=True, blank=True)
    lastname = models.CharField(max_length=45, null=True, blank=True)
    phonenumber = models.CharField(max_length=45, null=True, blank=True)
    mail = models.CharField(max_length=255)
    cp = models.CharField(max_length=45, null=True, blank=True)
    city = models.CharField(max_length=45, null=True, blank=True)
    adresse = models.CharField(max_length=45, null=True, blank=True)
    country = models.CharField(max_length=45, null=True, blank=True)
    user = models.ForeignKey(User)
    creationdate = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    modificationdate = models.DateTimeField(null=True)
    def __str__(self):
        return u"%s" % self.mail


class Estimate(models.Model):
    creationdate = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    modificationdate = models.DateTimeField(null=True)
    nb = models.FloatField(null=True, blank=True)
    price_with_tax = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    price_without_tax = models.DecimalField(max_digits=10, decimal_places=0 ,null=True, blank=True)
    type_guyot = models.CharField(max_length=2,null=True, blank=True)
    largeur_entre_rangs = models.DecimalField(max_digits=10, decimal_places=3,null=True, blank=True)
    distance_entre_ceps = models.DecimalField(max_digits=10, decimal_places=3,null=True, blank=True)
    surface = models.DecimalField(max_digits=10, decimal_places=3,null=True, blank=True)
    plant_superficie = models.CharField(max_length=3,null=True, blank=True)
    customer = models.ForeignKey(Customer)
    def __str__(self):
        return u"%s et %s" % (self.customer,self.creationdate)

class Benefit(models.Model):
    unit_price = models.DecimalField(max_digits=10, decimal_places=3,null=True, blank=True)    
    unit_type = models.CharField(max_length=45, blank=True)
    price_with_tax = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    price_without_tax = models.DecimalField(max_digits=10, decimal_places=0 ,null=True, blank=True)
    tax = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    modificationdate = models.DateTimeField(null=True, blank=True)
    activity = models.ForeignKey(ActivityPrestaViticole)
    estimate = models.ForeignKey(Estimate, related_name='estimates', related_query_name='estimate')
