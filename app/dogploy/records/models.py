from django.db import models

class Vet(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    def introduce(self):
        return "Hello, I am {} {}".format(self.first_name, self.last_name)

class Animal(models.Model):
    species = models.CharField(max_length=30)
    age = models.IntegerField()
    owner = models.CharField(max_length=30)
    def introduce(self):
        return "I am a {}-year old {} owned by {}".format(self.age, self.species, self.owner)

class Owner(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    def introduce(self):
        return "I am {} and I live at: {}".format(self.name, self.address)
