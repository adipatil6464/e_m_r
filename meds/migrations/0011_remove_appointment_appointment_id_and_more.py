# Generated by Django 4.2.3 on 2023-10-14 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meds', '0010_alter_appointmentid_appointment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_id',
        ),
        migrations.DeleteModel(
            name='AppointmentId',
        ),
    ]
