# Generated by Django 4.2.3 on 2023-10-14 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meds', '0008_appointmentid_appointment_appointment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentid',
            name='appointment_id',
            field=models.IntegerField(default=20),
        ),
    ]