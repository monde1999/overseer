from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, authenticate

from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.decorators import api_view

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.none()
    serializer_class = UserSerializer


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    f = authenticate(request, username=username, password=password)   
    flag = 'false'
    if f is not None:   
        flag = 'true'
    else:
        queryset = User.objects.filter(username=username)
        if len(queryset) > 0:
            flag = 'wrong_password'
    content = {
        'flag': flag
    }
    return Response(content)
    