# Generated by Django 4.2 on 2023-04-15 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpApp', '0007_alter_empmodel_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empmodel',
            name='photo',
            field=models.TextField(blank=True, null=True),
        ),
    ]