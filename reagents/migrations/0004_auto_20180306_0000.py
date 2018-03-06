# Generated by Django 2.0.2 on 2018-03-06 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0003_auto_20180305_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='biologics',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reagents.Biologic'),
        ),
        migrations.AddField(
            model_name='solution',
            name='liquids',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reagents.Liquid'),
        ),
        migrations.AddField(
            model_name='solution',
            name='solids',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reagents.Solid'),
        ),
        migrations.AddField(
            model_name='solution',
            name='solutions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reagents.Solution'),
        ),
    ]
