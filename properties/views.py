from rest_framework import generics
from .models import Property
from .serializers import PropertySerializer
from .utils import get_all_properties

class PropertyListCreateView(generics.ListCreateAPIView):
    serializer_class = PropertySerializer

    def get_queryset(self):
        return get_all_properties()
    
    def perform_create(self, serializer):
        instance = serializer.save()
        # Invalidate cache on new property creation
        from django.core.cache import cache
        cache.delete("all_properties")
        return instance
