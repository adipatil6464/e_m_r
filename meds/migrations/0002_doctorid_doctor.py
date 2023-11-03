# Generated by Django 4.2.3 on 2023-09-17 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctorId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorid', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=100)),
                ('doctor_mail', models.EmailField(max_length=254, unique=True)),
                ('doctor_age', models.IntegerField()),
                ('doctor_address', models.CharField(max_length=100)),
                ('doctor_password', models.CharField(max_length=100)),
                ('doctor_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='meds.doctorid')),
            ],
        ),
    ]
