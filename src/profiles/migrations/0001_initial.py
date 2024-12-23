# Generated by Django 5.1.3 on 2024-12-08 01:37

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "is_enabled",
                    models.BooleanField(default=False, help_text="알림 활성화 여부"),
                ),
                ("notification_dtm", models.TimeField(default=datetime.time(8, 0))),
            ],
            options={
                "db_table": "notifications",
            },
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("profile_photo_url", models.URLField(blank=True, null=True)),
                (
                    "profile_photo_file",
                    models.ImageField(blank=True, null=True, upload_to="profile_photo"),
                ),
                (
                    "notification",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notification",
                        to="profiles.notification",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "user_profile",
                "constraints": [models.UniqueConstraint(fields=("user",), name="user foreign key")],
            },
        ),
    ]
