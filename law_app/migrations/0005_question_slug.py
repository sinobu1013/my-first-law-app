# Generated by Django 4.0.6 on 2022-11-23 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law_app', '0004_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
