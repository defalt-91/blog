from rest_framework import serializers
from .models import post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = ('author', 'id', 'title', 'content', 'date_posted')
