# Generated by Django 5.1.3 on 2024-12-05 18:25

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("event_calendar", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ShareImage",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(editable=False, primary_key=True, serialize=False),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "calendar_dt",
                    models.DateField(blank=True, help_text="캘린더 날짜", null=True),
                ),
                (
                    "share_image",
                    models.ImageField(help_text="사용자 공유 이미지", upload_to="share_image"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="share_image",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "share_image",
            },
        ),
    ]