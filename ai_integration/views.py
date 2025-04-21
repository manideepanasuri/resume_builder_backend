from django.contrib.messages.api import success
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .ai_latexgeneration import *
from user_details.models import UserDetailsCollage


# Create your views here.

class AiLatexGeneration(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        jobdescription=request.data.get('jobdescription')
        template=request.data.get('template')
        user=request.user
        if template is None:
            data={
                "success":"false",
                'message':"Failed to Generate"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        try:
            latexcode=gen_resume(user,jobdescription,template)
            data={
                "success":"true",
                "message":"Successfully Generated",
                "latexcode":latexcode
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                "success":"false",
                "message":"Failed to Generate",
            }
            print(e)
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


