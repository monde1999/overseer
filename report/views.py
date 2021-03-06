from django.shortcuts import render
from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import MultiPartParser

@api_view(['GET'])
def apiOverview(request):
    ervin= {
        'e':1,
        'r':2,
    }
    return Response(ervin)

@api_view(['POST'])
def createUser(request):
    userSerializer=UserSerializer(data=request.data)
    if userSerializer.is_valid():
        userSerializer.save()
    
    return Response(userSerializer.data)


@api_view(['POST'])
@parser_classes([MultiPartParser])
def createReport(request):

    reportSerializer=ReportSerializer(data=request.data)
    if reportSerializer.is_valid():
        reportSerializer.save()
    
    return Response(reportSerializer.data)


