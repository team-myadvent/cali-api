# Generated by Django 5.1.3 on 2024-12-08 10:19

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
            name="ShareImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(editable=False, primary_key=True, serialize=False),
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
        migrations.CreateModel(
            name="YoutubeMusicEvent",
            fields=[
                (
                    "id",
                    models.BigAutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "video_id",
                    models.CharField(
                        blank=True,
                        help_text="유튜브 비디오 아이디",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "music_url",
                    models.URLField(
                        blank=True,
                        help_text="유튜브 비디오 링크",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "thumbnail_url",
                    models.URLField(
                        blank=True,
                        help_text="유튜브 섬네일 링크",
                        max_length=255,
                        null=True,
                    ),
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
                    "id",
                    models.BigAutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("calendar_dt", models.DateField(help_text="캘린더 날짜")),
                (
                    "seq_no",
                    models.IntegerField(default=0, help_text="캘린더 인덱스 번호"),
                ),
                (
                    "title",
                    models.CharField(default="", help_text="유튜브 음악 제목", max_length=255),
                ),
                (
                    "comment",
                    models.CharField(help_text="이미지 표현 될 메시지", max_length=100),
                ),
                (
                    "comment_detail",
                    models.TextField(blank=True, help_text="캘린더 메시지", null=True),
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
