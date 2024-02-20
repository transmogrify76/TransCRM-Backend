<<<<<<< HEAD
# Generated by Django 5.0.2 on 2024-02-19 05:29
=======
# Generated by Django 5.0.2 on 2024-02-19 05:02
>>>>>>> 8a9f1c279f1e0e9065e99ff2e1740fed97a48425

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
<<<<<<< HEAD
                ('email', models.EmailField(max_length=254)),
=======
>>>>>>> 8a9f1c279f1e0e9065e99ff2e1740fed97a48425
                ('visiting_date', models.DateField()),
                ('prospect_status', models.CharField(max_length=255)),
                ('outcome', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.role'),
        ),
    ]
