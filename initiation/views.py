from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur ma Page !</h1>
        <p>Ceci est une initiation sur le framework Django!</p>
    """)
from django.shortcuts import render

# Create your views here.
