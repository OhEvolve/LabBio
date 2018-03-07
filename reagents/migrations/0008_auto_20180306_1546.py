# Generated by Django 2.0.2 on 2018-03-06 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0007_auto_20180306_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='solid',
            name='mw_units',
            field=models.CharField(choices=[('kg/mol', 'kg/mol'), (' g/mol', ' g/mol')], default=' g/mol', max_length=4),
        ),
        migrations.AlterField(
            model_name='biologiccontent',
            name='reagent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reagents.Biologic'),
        ),
        migrations.AlterField(
            model_name='biologiccontent',
            name='solution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reagents.Solution'),
        ),
        migrations.AlterField(
            model_name='liquidcontent',
            name='reagent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reagents.Liquid'),
        ),
        migrations.AlterField(
            model_name='liquidcontent',
            name='solution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reagents.Solution'),
        ),
        migrations.AlterField(
            model_name='solid',
            name='mw',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='solidcontent',
            name='reagent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reagents.Solid'),
        ),
        migrations.AlterField(
            model_name='solidcontent',
            name='solution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reagents.Solution'),
        ),
    ]