# cities/urls.py
from django.urls import path

from .views import *

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
    path('analytics', analytic, name="analytic"), # analytics
    path('analytics/<int:id>/', analytics, name="analytics"), #
    path('Anthropometry', myAnthropometry, name="Anthropometry"), # Anthropometry
    path('Anthropometrys/<int:id>/', myAnthropometrys, name="Anthropometrys"), #
    path('Computer', myComputer, name="Computer"), # Computer
    path('Computers/<int:id>/', myComputers, name="Computers"), #
    path('Distribution', myDistribution, name="Distribution"), # Distribution
    path('Distributions/<int:id>/', myDistributions, name="Distributions"), #
    path('Human', myHuman, name="Human"), # Human
    path('Humans/<int:id>/', myHumans, name="Humans"), #
    path('Management', myManagement, name="Management"), # Management
    path('Managements/<int:id>/', myManagements, name="Managements"), #
    path('Manufacturing', myManufacturing, name="Manufacturing"), # Manufacturing
    path('Manufacturings/<int:id>/', myManufacturings, name="Manufacturings"), #
    path('Operation', myOperation, name="Operation"), # Operation
    path('Operations/<int:id>/', myOperations, name="Operations"), #
    path('Quality', myQuality, name="Quality"), # Quality
    path('Qualitys/<int:id>/', myQualitys, name="Qualitys"), #
]