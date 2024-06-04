from django.shortcuts import render  # noqa
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def test(request):
    print(request.user)
    return Response({'message': 'Hello, world!'})
