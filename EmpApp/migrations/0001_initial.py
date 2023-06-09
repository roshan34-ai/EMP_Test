# Generated by Django 4.2 on 2023-04-12 12:41

import EmpApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpModel',
            fields=[
                ('regid', models.CharField(default=EmpApp.models.create_id, editable=False, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('phoneNo', models.CharField(max_length=100)),
                ('addressDetails', models.CharField(max_length=100)),
                ('houseNo', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('workExperience', models.CharField(max_length=100)),
                ('componyName', models.CharField(max_length=100)),
                ('fromDate', models.DateField()),
                ('toDate', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('qualifications', models.CharField(max_length=100)),
                ('qualificationName', models.CharField(max_length=100)),
                ('percentage', models.DecimalField(decimal_places=1, max_digits=3)),
                ('projects', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('photo', models.FileField(upload_to='')),
            ],
        ),
    ]
