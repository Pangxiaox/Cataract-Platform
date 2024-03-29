# Generated by Django 2.2.5 on 2019-09-15 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InformTable', '0005_auto_20190915_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='essentialinformation',
            name='marriage',
        ),
        migrations.AddField(
            model_name='essentialinformation',
            name='marriage_history',
            field=models.CharField(choices=[('是', 'yes'), ('否', 'no')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='marriage',
            field=models.CharField(choices=[('已婚', 'true'), ('未婚', 'false')], max_length=2),
        ),
    ]
