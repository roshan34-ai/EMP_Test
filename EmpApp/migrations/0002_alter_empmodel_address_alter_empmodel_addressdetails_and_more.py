# Generated by Django 4.2 on 2023-04-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empmodel',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='addressDetails',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='componyName',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='email',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='fromDate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='gender',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='houseNo',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='percentage',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='phoneNo',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='photo',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='projects',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='qualificationName',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='qualifications',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='street',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='toDate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='workExperience',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
