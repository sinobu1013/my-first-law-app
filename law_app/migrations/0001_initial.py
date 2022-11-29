# Generated by Django 4.0.6 on 2022-11-16 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('field_name', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='分野の名前')),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Generation',
            fields=[
                ('generation', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='授業タイトル')),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Qformat',
            fields=[
                ('format_id', models.IntegerField(primary_key=True, serialize=False)),
                ('format_name', models.CharField(max_length=255, verbose_name='問題の種類')),
            ],
        ),
    ]
