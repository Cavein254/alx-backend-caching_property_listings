from django.urls import path
from .views import PropertyListCreateView, property_list

urlpatterns = [
    path('properties/', property_list, name='property-list'),
    path('properties-crud/', PropertyListCreateView.as_view(), name='property-list-create'),

]
