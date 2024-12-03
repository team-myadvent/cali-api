# Generated by Django 5.1.3 on 2024-12-03 20:15

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="YoutubeMusicEvent",
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
                ("music_url", models.URLField(blank=True, max_length=255, null=True)),
                (
                    "thumbnail_url",
                    models.URLField(blank=True, max_length=255, null=True),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="youtube_music",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "youtube_music",
            },
        ),
        migrations.CreateModel(
            name="EventCalendar",
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
                ("calendar_dt", models.DateField(help_text="캘린더 날짜")),
                (
                    "title",
                    models.CharField(default="", help_text="이미지에 표현 될 메시지", max_length=20),
                ),
                (
                    "comment",
                    models.CharField(help_text="캘린더에 등록 될 메시지", max_length=20),
                ),
                (
                    "is_shareable",
                    models.BooleanField(default=False, help_text="캘린더 공유하기 여부"),
                ),
                (
                    "share_key",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="외부 사용자 접근 키",
                    ),
                ),
                ("default_image", models.URLField(help_text="캘린더 기본 이미지")),
                (
                    "thumbnail_file",
                    models.ImageField(
                        blank=True,
                        help_text="캘린더 사용자 등록 이미지",
                        null=True,
                        upload_to="calendar_thumbnail",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="calendar",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "youtube",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="yotubue",
                        to="event_calendar.youtubemusicevent",
                    ),
                ),
            ],
            options={
                "db_table": "event_calendar",
            },
        ),
    ]
