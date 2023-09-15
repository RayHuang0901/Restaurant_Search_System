from django.db import models

# Create your models here.

class Positions(models.Model):
    Name = models.CharField(max_length=100,null=True)
    Area = models.CharField(max_length=100,null=True)
    Road = models.CharField(max_length=100,null=True)
    Door_num = models.CharField(max_length=100,null=True)
    Floor = models.CharField(max_length=100,null=True)

class Prices(models.Model):
    Name = models.CharField(max_length=100,null=True)
    Service_charge = models.CharField(max_length=100,null=True)
    min_charge = models.CharField(max_length=100,null=True)
    Avg_charge = models.CharField(max_length=100,null=True)
  
class Food_Type(models.Model):
    Name = models.CharField(max_length=100,null=True)
    Type = models.CharField(max_length=100,null=True)
    Style = models.CharField(max_length=100,null=True)
    Veg = models.CharField(max_length=100,null=True)
  
class Infos(models.Model):
    Name = models.CharField(max_length=100,null=True)
    START_Time = models.TimeField(auto_now=False, auto_now_add=False)
    Close_Time = models.TimeField(auto_now=False, auto_now_add=False)
    Menu = models.CharField(max_length=100,null=True)
    FB = models.CharField(max_length=100,null=True)
    Phone = models.CharField(max_length=100,null=True)

class Comment(models.Model):
    Name = models.CharField(max_length=100,null=True)
    CP = models.CharField(max_length=100,null=True)
    Service = models.CharField(max_length=100,null=True)
    Delicious_level = models.CharField(max_length=100,null=True)
    Clean = models.CharField(max_length=100,null=True)