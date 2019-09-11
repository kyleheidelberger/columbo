# Generated by Django 2.2.5 on 2019-09-11 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('columboAPI', '0003_auto_20190911_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='director',
        ),
        migrations.AddField(
            model_name='episode',
            name='director',
            field=models.ManyToManyField(default='', to='columboAPI.Director'),
        ),
        migrations.RemoveField(
            model_name='episode',
            name='writer',
        ),
        migrations.AddField(
            model_name='episode',
            name='writer',
            field=models.ManyToManyField(default='', to='columboAPI.Writer'),
        ),
    ]
