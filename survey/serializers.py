from rest_framework import serializers
from .models import Choices, Survey


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['question','id']


class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = ['choicefield', 'rel']
