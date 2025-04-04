# Generated by Django 5.1.2 on 2025-04-01 12:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer_system", "0005_careappointment_user"),
        ("personnel_management", "0002_appointmentmatch"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="careappointment",
            name="employee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="personnel_management.employee",
            ),
        ),
        migrations.AlterField(
            model_name="careappointment",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="careappointments",
                to="customer_system.customerprofile",
            ),
        ),
        migrations.AlterField(
            model_name="careappointment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="careappointments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
