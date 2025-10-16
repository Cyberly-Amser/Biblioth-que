from django.urls import path
from . import views

urlpatterns = [
    path('catalogue/accueil.html', views.accueil, name='Page_d_accueil')
]