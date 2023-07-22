from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import newsModel
from .serializers import newsSerializer
# Create your views here.
class newsAllView(ListAPIView):
    queryset = newsModel.objects.all()
    serializer_class = newsSerializer