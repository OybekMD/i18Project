from modeltranslation.translator import translator, TranslationOptions, register
from news.models import journalistModel, newsModel

class journalistTranslationOptions(TranslationOptions):
    fields = ('name', 'text',)

translator.register(newsModel, journalistTranslationOptions)
