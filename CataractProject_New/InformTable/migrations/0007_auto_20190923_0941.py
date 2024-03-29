# Generated by Django 2.2.5 on 2019-09-23 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InformTable', '0006_auto_20190923_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eyeexamine',
            name='left_anteriorchamber_central',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eyeexamine',
            name='left_anteriorchamber_surrounded',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eyeexamine',
            name='left_intraocularpressure',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eyeexamine',
            name='left_pupil_diameter',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eyeexamine',
            name='left_vision',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eyeexamine',
            name='right_anteriorchamber_central',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eyeexamine',
            name='right_anteriorchamber_surrounded',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eyeexamine',
            name='right_intraocularpressure',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eyeexamine',
            name='right_pupil_diameter',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eyeexamine',
            name='right_vision',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
