# Generated by Django 5.0 on 2023-12-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management_app', '0004_employee_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id_proof',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]