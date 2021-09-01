from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'accounts', views.UserViewSet)
# router.register(r'login', views.LoginViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]