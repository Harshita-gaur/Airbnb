from django.urls import path
from .views import get_or_create_properties

urlpatterns = [
    path('api/listings/', get_or_create_properties, name='get_properties'),

]
