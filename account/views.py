from rest_framework import viewsets
from django.contrib.auth.models import User
# from .serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, authenticate

from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.decorators import api_view

from rest_framework.authtoken.models import Token

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.none()
#     serializer_class = UserSerializer

@api_view(["POST"])
def signup(request):
    usr = request.data.get('username')
    pw = request.data.get('password')
    fname = request.data.get('firstName')
    lname = request.data.get('lastName')
    # email = request.data.get('email')

    flag = 'false'
    new_user = None
    token_key=''
    if usr != '' and pw != '': # validation here
        queryset = User.objects.filter(username=usr)
        if (len(queryset)==0):
            new_user = User(username=usr,first_name=fname, last_name=lname)
        if new_user is not None:
            new_user.set_password(pw)
            new_user.save()
            flag = 'true'
            token:Token = Token.objects.create(user=new_user)
            token_key = token.key
    
    context = {
        'flag': flag,
        'token': token_key
    }

    return Response(context)


@api_view(["POST"])
def login(request):
    token_key = ''
    username = request.data.get("username")
    password = request.data.get("password")
    f = authenticate(request, username=username, password=password)  
    flag = 'false'
    if f is not None:   
        flag = 'true'
        token_key = Token.objects.get_or_create(user=f)[0].key
    else:
        queryset = User.objects.filter(username=username)
        if len(queryset) > 0:
            flag = 'wrong_password'
    content = {
        'flag': flag,
        'token':token_key
    }
    return Response(content)
    