from django.contrib import admin
from .models import Vet, Animal, Owner

# Register your models here.

admin.site.register(Vet)
admin.site.register(Animal)
admin.site.register(Owner)
