from django.shortcuts import render

# Create your views here.

'''
#from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
'''



from .models import RestapiTutorial
from rest_framework.response import Response
from rest_framework.decorators import api_view
from  .serializers import Tutorial1Serializer
from rest_framework import status


@api_view(['GET', 'POST'])
def tutorial_list(request):
    """
    List all code tutorials, or create a new tutorial.
    """
    if request.method == 'GET':
        tutorials = RestapiTutorial.objects.all()
        serializer = Tutorial1Serializer(tutorials, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = Tutorial1Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = RestapiTutorial.objects.get(pk=pk)
    except RestapiTutorial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Tutorial1Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Tutorial1Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)