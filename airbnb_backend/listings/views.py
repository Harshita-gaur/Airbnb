from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import AirbnbListing
from .serializers import AirbnbListingSerializer

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
