from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import AirbnbListing
from .serializers import AirbnbListingSerializer
from django.db.models import Q


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])  
def get_or_create_properties(request):
    if request.method == 'GET':
        properties = AirbnbListing.objects.all()
        serializer = AirbnbListingSerializer(properties, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AirbnbListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



@api_view(["GET"])
def search_listings(request):
    location = request.GET.get("location", "")
    min_price = request.GET.get("min_price", 0)
    max_price = request.GET.get("max_price", 999999)

    listings = AirbnbListing.objects.filter(
        Q(location__icontains=location),
        Q(price_per_night__gte=min_price),
        Q(price_per_night__lte=max_price),
    )

    serializer = AirbnbListingSerializer(listings, many=True)
    return Response(serializer.data)
