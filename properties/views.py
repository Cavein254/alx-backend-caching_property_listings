from rest_framework import generics
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from django.http import JsonResponse
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

@api_view(["GET"])
@cache_page(60 * 15)  # cache for 15 minutes
def property_list(request):
    if request.method == "GET":
        properties = Property.objects.all().order_by("-created_at")
        serializer = PropertySerializer(properties, many=True)
        return JsonResponse(serializer.data, safe=False)
