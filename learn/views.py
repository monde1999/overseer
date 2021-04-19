from django.shortcuts import render
from django.http import HttpResponse
from .models import BehaviorAnalyzer

# Create your views here.

# ba = BehaviorAnalyzer()
# ba.start()

def post_location(request):
    x = request.GET.get('x', None)
    y = request.GET.get('y', None)
    print('x = ', x, ', y = ', y)
    if (x is None or y is None):
        return HttpResponse('Fail!')
    else:
        return HttpResponse('Success!')