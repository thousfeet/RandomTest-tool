# Generated by Django 2.0.4 on 2018-04-20 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testTool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='matchId',
            field=models.IntegerField(default=0),
        ),
    ]
