
from django.shortcuts import render, redirect
from initiation.models import Name
from initiation.forms import NameForm

# Create your views here.

def index(request):
    listes_names = Name.objects.all()

    form = NameForm()

    context_dict = {'names_from_context': listes_names, 'form': form}

    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'index.html', context_dict)
        else:
            print(form.errors)    

    return render(request, 'index.html', context_dict)