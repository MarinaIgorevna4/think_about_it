# Generated by Django 4.0.3 on 2022-03-30 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0006_question_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(max_length=255, unique_for_date='publish'),
        ),
    ]
