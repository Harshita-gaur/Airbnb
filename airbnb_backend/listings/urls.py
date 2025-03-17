from django.urls import path
from .views import get_or_create_properties,search_listings

urlpatterns = [
    path('api/listings/', get_or_create_properties, name='get_properties'),
    path("api/search_listings/", search_listings),


]
