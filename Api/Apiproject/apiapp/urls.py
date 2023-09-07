from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.APIResponseView.as_view(), name = 'api_response')
]