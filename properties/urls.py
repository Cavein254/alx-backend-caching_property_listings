from django.urls import path
from .views import PropertyListCreateView, property_list, cache_metrics

urlpatterns = [
    path('properties/', property_list, name='property-list'),
    path('properties-crud/', PropertyListCreateView.as_view(), name='property-list-create'),
    path('cache-metrics/', cache_metrics, name='cache-metrics'),

]
