# Generated by Django 2.0.2 on 2018-03-06 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0006_auto_20180306_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biologiccontent',
            name='moles',
        ),
        migrations.RemoveField(
            model_name='solidcontent',
            name='moles',
        ),
        migrations.AddField(
            model_name='biologiccontent',
            name='mass_units',
            field=models.CharField(choices=[('ng/L', 'ng/L'), ('ug/L', 'ug/L'), ('mg/L', 'mg/L'), (' g/L', ' g/L'), (' nM ', ' nM '), (' uM ', ' uM '), (' mM ', ' mM '), ('  M ', '  M ')], default=' g/L', max_length=4),
        ),
        migrations.AddField(
            model_name='liquidcontent',
            name='volume_units',
            field=models.CharField(choices=[('uL', 'uL'), ('mL', 'mL'), (' L', ' L')], default=' L', max_length=2),
        ),
        migrations.AddField(
            model_name='solidcontent',
            name='mass_units',
            field=models.CharField(choices=[('ng/L', 'ng/L'), ('ug/L', 'ug/L'), ('mg/L', 'mg/L'), (' g/L', ' g/L'), (' nM ', ' nM '), (' uM ', ' uM '), (' mM ', ' mM '), ('  M ', '  M ')], default=' g/L', max_length=4),
        ),
        migrations.AlterField(
            model_name='biologiccontent',
            name='mass',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='liquidcontent',
            name='volume',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='solidcontent',
            name='mass',
            field=models.FloatField(default=0),
        ),
    ]
