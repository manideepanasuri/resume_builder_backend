from django.contrib import admin
from django.urls import path,include

from ai_integration.views import *

urlpatterns = [
   path('resume/',AiLatexGeneration.as_view(),name='resume'),
]
