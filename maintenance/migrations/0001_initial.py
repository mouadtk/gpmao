# Generated by Django 5.0.6 on 2024-05-29 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_id', models.CharField(max_length=50)),
                ('maintenance_date', models.DateField()),
                ('technician', models.CharField(max_length=100)),
                ('notes', models.TextField()),
            ],
        ),
    ]
