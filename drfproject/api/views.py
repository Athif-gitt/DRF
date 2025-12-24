from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def get_item(request):
    return Response(ItemSerializer({"name": "Bike", "description": "Used to ride!"}).data)

