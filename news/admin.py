from django.contrib import admin
from .models import journalistModel, newsModel
from .forms import newsForms
# Register your models here.
class newsAdmin(admin.ModelAdmin):
    form = newsForms
    list_display = ('name', 'text')
    search_fields = ('name',)

admin.site.register(journalistModel)
admin.site.register(newsModel, newsAdmin)
