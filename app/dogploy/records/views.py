from django.shortcuts import render


from .models import Vet, Animal, Owner

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

