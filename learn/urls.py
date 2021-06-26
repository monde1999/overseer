from django.urls import include, path
from . import views

urlpatterns = [
    path('post/', views.post_location, name='post_location'),
]