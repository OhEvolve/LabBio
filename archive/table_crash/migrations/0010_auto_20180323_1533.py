# Generated by Django 2.0.2 on 2018-03-23 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocols', '0009_auto_20180323_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protocol',
            name='inputs',
        ),
        migrations.RemoveField(
            model_name='protocol',
            name='outputs',
        ),
    ]
