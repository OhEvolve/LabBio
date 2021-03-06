# Generated by Django 2.0.2 on 2018-03-22 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0010_auto_20180322_2151'),
        ('protocols', '0006_auto_20180315_0005'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddedBiologic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mass', models.FloatField(default=0)),
                ('mass_units', models.CharField(choices=[('ng/L', 'ng/L'), ('ug/L', 'ug/L'), ('mg/L', 'mg/L'), (' g/L', ' g/L'), (' nM ', ' nM '), (' uM ', ' uM '), (' mM ', ' mM '), ('  M ', '  M ')], default=' g/L', max_length=4)),
                ('reagent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reagents.Biologic')),
            ],
        ),
        migrations.CreateModel(
            name='AddedLiquid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.FloatField(default=1)),
                ('volume_units', models.CharField(choices=[('uL', 'uL'), ('mL', 'mL'), (' L', ' L')], default=' L', max_length=2)),
                ('reagent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reagents.Liquid')),
            ],
        ),
        migrations.CreateModel(
            name='AddedSolid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mass', models.FloatField(default=0)),
                ('mass_units', models.CharField(choices=[('ng/L', 'ng/L'), ('ug/L', 'ug/L'), ('mg/L', 'mg/L'), (' g/L', ' g/L'), (' nM ', ' nM '), (' uM ', ' uM '), (' mM ', ' mM '), ('  M ', '  M ')], default=' g/L', max_length=4)),
                ('reagent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reagents.Solid')),
            ],
        ),
        migrations.CreateModel(
            name='OperateStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='protocol',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='protocol',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='step',
            name='reagents',
        ),
        migrations.AddField(
            model_name='step',
            name='action',
            field=models.CharField(choices=[('-------', '-----'), ('Discard', 'Discard'), ('  Save ', 'Save')], default='-------', max_length=7),
        ),
        migrations.AddField(
            model_name='step',
            name='container',
            field=models.CharField(default='1.5mL Tube', max_length=30),
        ),
        migrations.AddField(
            model_name='thermocyclestep',
            name='goto_step',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='thermocyclestep',
            name='repeats',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='thermocyclestep',
            name='stage_type',
            field=models.CharField(choices=[('----', '----'), ('Hold', 'Hold'), ('Goto', 'Goto')], default='Hold', max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='operatestep',
            name='step',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='protocols.Step'),
        ),
        migrations.AddField(
            model_name='addedsolid',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protocols.Step'),
        ),
        migrations.AddField(
            model_name='addedliquid',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protocols.Step'),
        ),
        migrations.AddField(
            model_name='addedbiologic',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protocols.Step'),
        ),
        migrations.AddField(
            model_name='step',
            name='biologics',
            field=models.ManyToManyField(through='protocols.AddedBiologic', to='reagents.Biologic'),
        ),
        migrations.AddField(
            model_name='step',
            name='liquids',
            field=models.ManyToManyField(through='protocols.AddedLiquid', to='reagents.Liquid'),
        ),
        migrations.AddField(
            model_name='step',
            name='solids',
            field=models.ManyToManyField(through='protocols.AddedSolid', to='reagents.Solid'),
        ),
    ]
