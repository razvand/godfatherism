from django.shortcuts import render
from django.utils import timezone
from .models import Person

# Create your views here.
def index(request):
    persons = Person.objects.select_related().all()
    return render(request, 'kinship/index.html', {'persons':persons})
