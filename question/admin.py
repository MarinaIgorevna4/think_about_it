from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(models.Question)

admin.site.register(models.Answer)
admin.site.register(models.Profile)


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('main_question', 'publish_question')
    list_filter = ('publish_question', )
    search_fields = ('main_question', )
    prepopulated_fields = {'slug': ('publish_question', )}