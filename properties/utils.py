from django.core.cache import cache
from .models import Property

CACHE_KEY = "all_properties"
CACHE_TIMEOUT = 3600  # 1 hour in seconds

def get_all_properties():
    # Try to fetch from cache
    properties = cache.get(CACHE_KEY)

    if properties is None:
        # Cache miss → fetch from DB
        properties = list(Property.objects.all())
        # Save to cache
        cache.set(CACHE_KEY, properties, CACHE_TIMEOUT)

    return properties
