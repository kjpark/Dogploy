from django.contrib import admin
from .models import Vet, Animal, Owner

# Register your models here.

admin.site.register(Vet)
admin.site.register(Animal)
admin.site.register(Owner)

class VetAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']


admin.site.register(Vet, VetAdmin)
