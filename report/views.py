from report.models import Reaction, Report_Image
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes,parser_classes
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from django.core.files import File
from rest_framework.permissions import IsAuthenticated

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
@parser_classes([MultiPartParser,JSONParser])
def saveReport(request):

    print(request.method)
    print(request.data)
    r = Report(user = User.objects.get(id = request.data['user']),
    description = request.data['description'], 
    floodLevel = request.data['floodLevel'],
    latitude = request.data['latitude'],
    longitude = request.data['longitude'])
    
    r.save()
    
    print(request.FILES.getlist('ReportImages'))

    if request.FILES.get('ReportImages') is not None:
        for image in request.FILES.getlist('ReportImages'):
            file = File(image)
            Report_Image(image = File(image), report = r).save()

    return Response("Success")

@api_view(['POST'])
def reactToReport(request):
    
    print(request.POST)

    report = Report.objects.get(id = request.data['report'])
    user = User.objects.get(id = request.data['user'])
    isPositive = request.data['isPositive']

    Reaction(report=report,user=user,isPositive=isPositive).save()

    return Response(request.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def testReport(request):
    print(request.user)
    return Response("Success")


