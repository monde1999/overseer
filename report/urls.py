from django.urls import path
from . import views

app_name='report'
urlpatterns = [
    path('api-view/',views.apiOverview,name="api_view"),
    path('create-user/',views.createUser,name="create_user_view"),
    path('create-report/',views.saveReport,name="create_report_view"),
    path('react-to-report/',views.reactToReport,name="react_to_report_view"),
    path('test-report/',views.testReport,name="test_report_view")
]