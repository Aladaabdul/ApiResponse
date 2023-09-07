from django.shortcuts import render
from rest_framework import generics
from .models import ApiResponse
from .serializers import ApiResponseSerializer
from django.http import HttpResponseBadRequest
import datetime


# Create your views here.

class APIResponseView(generics.RetrieveAPIView):
    serializer_class = ApiResponseSerializer

    def get_object(self):

        utc_time = datetime.datetime.utcnow()
        api_response = ApiResponse (
            slack_name = 'Yakub Abdulrahman Alada',
            current_day = datetime.datetime.now().strftime('%A'),
            utc_time = utc_time,
            track = 'Backend',
            github_file_url = 'https://github.com/Aladaabdul/ApiResponse/blob/main/Api/Apiproject/apiapp/views.py',
            github_repo_url = 'https://github.com/Aladaabdul/ApiResponse.git'
        )
        return api_response