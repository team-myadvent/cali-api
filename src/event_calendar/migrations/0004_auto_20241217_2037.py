# Generated by Django 5.1.4 on 2024-12-17 20:37
import json

from django.db import migrations
from django.conf import settings
from datetime import date
from pathlib import Path

from config.settings.storages import S3_IMAGE_URL

TODAY = date.today()
MONTH = 12
MAX_DAYS = 26
YEAR = TODAY.year


def create_default_calendar(apps, schema_editor):
    Youtube = apps.get_model("event_calendar", "YoutubeMusicEvent")
    Calendar = apps.get_model("event_calendar", "EventCalendar")
    thumbnail_format = "https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

    json_path = Path(settings.ROOT_DIR, "src", "config", "default_music.json")

    with open(json_path, encoding="utf-8") as file:
        default_data = json.load(file)

    for day, data in enumerate(default_data, start=1):
        thumbnail = data.get("thumbnail")

        if not thumbnail:
            thumbnail = thumbnail_format.format(video_id=data["video_id"])

        youtube_music = Youtube.objects.create(
            user=None,
            video_id=data["video_id"],
            thumbnail_url=thumbnail,
        )

        Calendar.objects.create(
            user=None,
            youtube=youtube_music,
            calendar_dt=date(YEAR, MONTH, day),
            seq_no=day,
            title=data["title"],
            comment=data["comment"],
            comment_detail=data["comment_detail"],
            default_image=S3_IMAGE_URL.format(seq=day),
            thumbnail_file="",
        )


class Migration(migrations.Migration):
    dependencies = [
        ("event_calendar", "0003_alter_eventcalendar_options_alter_eventcalendar_user_and_more"),
    ]

    operations = [
        migrations.RunPython(create_default_calendar, reverse_code=migrations.RunPython.noop),
    ]