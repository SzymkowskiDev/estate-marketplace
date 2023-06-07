# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Buyers(models.Model):
    buyer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buyers'


class Offers(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    footer = models.FloatField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    price_per_meter = models.IntegerField(blank=True, null=True)
    number_of_rooms = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    floor = models.CharField(max_length=255, blank=True, null=True)
    rent = models.IntegerField(blank=True, null=True)
    remote_service = models.BooleanField(blank=True, null=True)
    form_of_ownership = models.CharField(max_length=255, blank=True, null=True)
    finishing_condition = models.CharField(max_length=255, blank=True, null=True)
    balcony_garden_terrace = models.CharField(max_length=255, blank=True, null=True)
    parking_space = models.CharField(max_length=255, blank=True, null=True)
    heating = models.CharField(max_length=255, blank=True, null=True)
    market = models.CharField(max_length=255, blank=True, null=True)
    advertiser_type = models.CharField(max_length=255, blank=True, null=True)
    available_from = models.CharField(max_length=255, blank=True, null=True)
    year_of_construction = models.IntegerField(blank=True, null=True)
    type_of_construction = models.CharField(max_length=255, blank=True, null=True)
    windows = models.CharField(max_length=255, blank=True, null=True)
    elevator = models.BooleanField(blank=True, null=True)
    media = models.CharField(max_length=255, blank=True, null=True)
    security = models.CharField(max_length=255, blank=True, null=True)
    equipment = models.CharField(max_length=255, blank=True, null=True)
    additional_infromation = models.CharField(max_length=255, blank=True, null=True)
    building_material = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    seller = models.ForeignKey('Sellers', models.DO_NOTHING, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offers'


class Sellers(models.Model):
    seller_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sellers'
