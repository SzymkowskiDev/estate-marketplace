from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.get_offers_data, name='offers-data'),
    path('map/', views.view_map, name='offers-map'),
]