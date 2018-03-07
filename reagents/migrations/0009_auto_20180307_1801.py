# Generated by Django 2.0.2 on 2018-03-07 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0008_auto_20180306_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solid',
            name='mw',
            field=models.FloatField(default=0, verbose_name='Molecular weight'),
        ),
        migrations.AlterField(
            model_name='solid',
            name='mw_units',
            field=models.CharField(choices=[('kg/mol', 'kg/mol'), (' g/mol', ' g/mol')], default=' g/mol', max_length=6, verbose_name='Units'),
        ),
    ]
