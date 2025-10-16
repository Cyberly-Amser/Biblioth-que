from ast import Return
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def accueil(request):
    contexte= {
        'heure':datetime.now(),
        
    }
    return render(request,'catalogue/accueil.html', contexte)