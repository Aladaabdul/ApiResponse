from django.shortcuts import render
from rest_framework import generics
from .models import ApiResponse
from .serializers import ApiResponseSerializer
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
        )
        return api_response