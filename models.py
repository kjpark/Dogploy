from django.db import models

class Vet(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    ID = models.IntegerField()

class Animal(models.Model):
    species = models.CharField(max_length=30)
    age = models.IntegerField()
    owner = models.CharField(max_length=30)

class Owner(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
