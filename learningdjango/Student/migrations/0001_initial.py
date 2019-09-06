# Generated by Django 2.2.5 on 2019-09-05 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('sex', models.CharField(choices=[('男', 'male'), ('女', 'female')], max_length=2)),
                ('credit', models.IntegerField(max_length=5)),
            ],
        ),
    ]
