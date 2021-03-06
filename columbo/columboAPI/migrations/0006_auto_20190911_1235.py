# Generated by Django 2.2.5 on 2019-09-11 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('columboAPI', '0005_auto_20190911_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='fun_facts',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='fun_facts',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='murderer',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='victim',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
