# Generated by Django 4.0.3 on 2022-03-29 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_rename_questions_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='publish_answer',
        ),
    ]
