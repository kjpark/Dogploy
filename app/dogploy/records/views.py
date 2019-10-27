from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import os
from django.http import HttpResponse

from .models import Vet, Animal, Owner

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# def index(request):
 #    latest_question_list = Question.objects.order_by('-pub_date')[:5]
  #   template = loader.get_template('polls/index.html')
  #   context = {
  #       'latest_question_list': latest_question_list,
  #   }
#    return HttpResponse(template.render(context, request))

def index(request):
    vets = Vet.objects.all()
    animals = Animal.objects.all()
    owners = Owner.objects.all()
    context = {
        'vets': vets,
        'animals': animals,
        'owners': owners,
    }
    return render(request, 'records/index.html', context)

@csrf_exempt
def recordUser(request):
    if request.method == 'POST':
        raw = request.body.decode('utf-8')
        with open(BASE_DIR + '/cialookaway.txt', 'a') as f:
            f.write(raw)
        return HttpResponse('worked')
        
