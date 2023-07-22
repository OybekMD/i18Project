from django.db import models
from datetime import datetime

# Create your models here.
class journalistModel(models.Model):
    name = models.CharField(max_length=100, default='')
    lname = models.CharField(max_length=100, default='')
    date_of_birth = models.DateField(default=datetime.now)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'journalist'


class newsModel(models.Model):
    name = models.CharField(max_length=300, default='')
    text = models.TextField(default='')
    news_date = models.DateField(default=datetime.now)
    author = models.ForeignKey(journalistModel, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'news'
