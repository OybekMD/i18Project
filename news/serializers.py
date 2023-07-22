from rest_framework import serializers
from .models import newsModel
class newsSerializer(serializers.ModelSerializer):
    class Meta:
        model = newsModel
        fields = ('name', 'text', 'news_date', 'author') 