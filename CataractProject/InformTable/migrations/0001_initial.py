# Generated by Django 2.2.5 on 2019-09-10 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EssentialInformation',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('main_suit', models.TextField()),
                ('medicalhistory_present', models.TextField()),
                ('tuberculosis_history', models.CharField(choices=[('是', 'yes'), ('否', 'no')], max_length=1)),
                ('hepatitis_history', models.CharField(choices=[('是', 'yes'), ('否', 'no')], max_length=1)),
                ('other_infectious_diseases_history', models.CharField(choices=[('是', 'yes'), ('否', 'no')], max_length=1)),
                ('chronic_disease_history', models.CharField(choices=[('是', 'yes'), ('否', 'no')], max_length=1)),
                ('hypertension_history', models.CharField(choices=[('是', 'yes'), ('否', 'no')], max_length=1)),
                ('diabetes_mellitus_history', models.CharField(choices=[('是', 'yes'), ('否', 'no')], max_length=1)),
                ('heart_disease_history', models.CharField(choices=[('是', 'yes'), ('否', 'no')], max_length=1)),
                ('vaccination_allergy_history', models.CharField(choices=[('是', 'yes'), ('否', 'no')], max_length=1)),
                ('surgery_history', models.CharField(choices=[('是', 'yes'), ('否', 'no')], max_length=1)),
                ('past_history_remarks', models.TextField()),
                ('birthplace', models.CharField(max_length=30)),
                ('smoking_hobbies', models.CharField(choices=[('是', 'yes'), ('否', 'no')], max_length=1)),
                ('drinking_hobbies', models.CharField(choices=[('是', 'yes'), ('否', 'no')], max_length=1)),
                ('epidemic_water_contact_history', models.CharField(choices=[('是', 'yes'), ('否', 'no')], max_length=1)),
                ('personal_history_remark', models.TextField()),
                ('marriage', models.CharField(choices=[('已婚', 'true'), ('未婚', 'false')], max_length=1)),
                ('marital_reproductive_history_remark', models.TextField()),
                ('menopause', models.CharField(choices=[('是', 'yes'), ('否', 'no')], max_length=1)),
                ('menstrual_history_remark', models.CharField(choices=[('是', 'yes'), ('否', 'no')], max_length=1)),
                ('diabetes_mellitus_family_history', models.CharField(choices=[('是', 'yes'), ('否', 'no')], max_length=1)),
                ('coronary_heart_disease_family_history', models.CharField(choices=[('是', 'yes'), ('否', 'no')], max_length=1)),
                ('stroke_family_history', models.CharField(choices=[('是', 'yes'), ('否', 'no')], max_length=1)),
                ('tumors_family_history', models.CharField(choices=[('是', 'yes'), ('否', 'no')], max_length=1)),
                ('hypertension_family_history', models.CharField(choices=[('是', 'yes'), ('否', 'no')], max_length=1)),
                ('family_history_remark', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[('男', 'male'), ('女', 'female')], max_length=2)),
                ('nation', models.CharField(max_length=10)),
                ('occupation', models.CharField(max_length=10)),
                ('marriage', models.CharField(choices=[('已婚', 'true'), ('未婚', 'false')], max_length=10)),
                ('birthplace', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('medicalhistory_reporter', models.CharField(max_length=10)),
                ('admission_date', models.DateField()),
                ('medicalhistory_recordtime', models.DateTimeField()),
            ],
        ),
    ]
