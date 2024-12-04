from .views import *
from django.urls import path

urlpatterns=[
    path('',CountryView.as_view(),name='country'),
    path('getCountry/<int:id>',CountryView.as_view(),name='country'),

    
]