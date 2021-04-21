from rest_framework import viewsets
from .models import Choices, Survey
from .serializers import ChoicesSerializer, SurveySerializer
from rest_framework import permissions


class ChoiceViewset(viewsets.ModelViewSet):
    queryset = Choices.objects.all()
    serializer_class = ChoicesSerializer


class SurveyViewset(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
