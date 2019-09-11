# Generated by Django 2.2.5 on 2019-09-11 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('columboAPI', '0002_auto_20190911_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='season',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='episode',
            name='season_num',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='episode',
            name='series_num',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='season',
            name='episodes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='season',
            name='number',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='season',
            name='year_aired',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
