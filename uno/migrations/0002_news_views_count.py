# Generated by Django 5.0.3 on 2024-03-20 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uno', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views_count',
            field=models.IntegerField(default=0, verbose_name='News Count'),
        ),
    ]