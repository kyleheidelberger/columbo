# Generated by Django 2.2.5 on 2019-09-11 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('columboAPI', '0006_auto_20190911_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='occupation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
