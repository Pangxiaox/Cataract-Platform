# Generated by Django 2.2.5 on 2019-09-15 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InformTable', '0007_auto_20190915_2044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='essentialinformation',
            old_name='birthplace',
            new_name='e_birthplace',
        ),
        migrations.RenameField(
            model_name='personalinformation',
            old_name='birthplace',
            new_name='p_birthplace',
        ),
    ]