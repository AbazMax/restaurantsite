# Generated by Django 4.1.1 on 2022-09-15 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_userreservation_req_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreservation',
            name='req_date',
            field=models.DateField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userreservation',
            name='req_time',
            field=models.TimeField(max_length=50),
        ),
    ]