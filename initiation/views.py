
from django.shortcuts import render, redirect
from initiation.models import Name

# Create your views here.

def index(request):
    listes_names = Name.objects.all()
    context_dict = {'names_from_context': listes_names}
    return render(request, 'index.html', context_dict)