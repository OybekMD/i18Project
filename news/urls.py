from django.urls import path
from .views import newsAllView

urlpatterns = [
    path('', newsAllView.as_view()),
]