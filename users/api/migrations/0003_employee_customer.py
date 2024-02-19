# Generated by Django 5.0.2 on 2024-02-15 03:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_role_remove_employee_user_delete_customer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.role')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('visiting_date', models.DateField()),
                ('prospect_status', models.CharField(max_length=255)),
                ('outcome', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employee')),
            ],
        ),
    ]