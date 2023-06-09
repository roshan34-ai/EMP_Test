# Generated by Django 4.2 on 2023-04-15 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpApp', '0005_alter_empmodel_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empmodel',
            name='address',
        ),
        migrations.RemoveField(
            model_name='empmodel',
            name='city',
        ),
        migrations.RemoveField(
            model_name='empmodel',
            name='componyName',
        ),
        migrations.RemoveField(
            model_name='empmodel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='empmodel',
            name='fromDate',
        ),
        migrations.RemoveField(
            model_name='empmodel',
            name='houseNo',
        ),
        migrations.RemoveField(
            model_name='empmodel',
            name='percentage',
        ),
        migrations.RemoveField(
            model_name='empmodel',
            name='qualificationName',
        ),
        migrations.RemoveField(
            model_name='empmodel',
            name='state',
        ),
        migrations.RemoveField(
            model_name='empmodel',
            name='street',
        ),
        migrations.RemoveField(
            model_name='empmodel',
            name='title',
        ),
        migrations.RemoveField(
            model_name='empmodel',
            name='toDate',
        ),
        migrations.AlterField(
            model_name='empmodel',
            name='photo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
