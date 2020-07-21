# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-23 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeldb", "0011_auto_20170214_1842"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobpost",
            name="closed_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="agencyapplicants",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Shortlisted", "Shortlisted"),
                    ("Selected", "Selected"),
                    ("Rejected", "Rejected"),
                    ("Process", "Process"),
                ],
                default="Pending",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="agencyrecruiterjobposts",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Shortlisted", "Shortlisted"),
                    ("Selected", "Selected"),
                    ("Rejected", "Rejected"),
                    ("Hired", "Hired"),
                    ("Process", "Process"),
                ],
                default="Pending",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="jobpost",
            name="previous_status",
            field=models.CharField(
                choices=[
                    ("Draft", "Draft"),
                    ("Exprired", "Expired"),
                    ("Live", "Live"),
                    ("Disabled", "Disabled"),
                    ("Pending", "Pending"),
                    ("Published", "Published"),
                    ("Hired", "Hired"),
                    ("Process", "Process"),
                ],
                default="Draft",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="jobpost",
            name="status",
            field=models.CharField(
                choices=[
                    ("Draft", "Draft"),
                    ("Exprired", "Expired"),
                    ("Live", "Live"),
                    ("Disabled", "Disabled"),
                    ("Pending", "Pending"),
                    ("Published", "Published"),
                    ("Hired", "Hired"),
                    ("Process", "Process"),
                ],
                max_length=50,
            ),
        ),
    ]
