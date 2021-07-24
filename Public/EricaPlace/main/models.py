from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.lookups import IsNull
# Create your models here.

class College(models.Model):
  name = models.CharField(max_length=45)

  def __str__(self):
    return self.name

class Building(models.Model):
  name = models.CharField(max_length=45)
  english_name = models.CharField(max_length=45, default='')
  photo = models.ImageField(upload_to = 'images/', null=True)
  code = models.CharField(max_length=45, default='')
  
  def __str__(self):
    return self.name

class Room(models.Model):
  name = models.CharField(max_length=45)
  subname = models.CharField(max_length=45, default='')
  capacity = models.IntegerField()
  photo = models.ImageField(upload_to = 'images/', null=True)
  equipment = models.TextField(null=True)
  college = models.ForeignKey(College, on_delete=CASCADE)
  building = models.ForeignKey(Building, on_delete=CASCADE)

  def __str__(self):
    return self.name

class Contacts(models.Model):
  category = models.CharField(max_length=45)
  building_name = models.CharField(max_length=45)
  phone_number = models.CharField(max_length=20)
  
  def __str__(self):
    return '['+self.category+'] '+self.building_name
