# Generated by Django 2.2.1 on 2019-09-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='sn_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='channel',
            name='tm_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
