from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(models.Question)

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('main_question', 'publish_question')
    search_fields = ('main_question', )
    prepopulated_fields = {'slug': ('publish_question', )}
