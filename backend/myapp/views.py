from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Pet

from django.shortcuts import render
from .serializer import *


def index(request):
    return render(request, "frontend/src/index.js", context={})

@api_view(['GET', 'POST'])
def pet_list(request):
    if request.method == 'GET':
        data = Pet.objects.all()

        serializer = PetSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['PUT', 'DELETE'])
def pets_detail(request, pk):
    try:
        pet = Pet.objects.get(pk=pk)
    except Pet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PetSerializer(pet, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)