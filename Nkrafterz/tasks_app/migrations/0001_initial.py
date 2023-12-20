# Generated by Django 5.0 on 2023-12-19 06:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee_management_app', '0009_rename_amount_salary_deduction_salary_gross_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('task_name', models.CharField(max_length=100)),
                ('descriptions', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_completed', models.BooleanField(default=True)),
                ('progress_percent', models.FloatField(default=0.0)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.employee')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks_app.task')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
