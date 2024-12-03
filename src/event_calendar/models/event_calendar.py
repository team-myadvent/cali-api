import uuid

from django.db import models
from django.contrib.auth import get_user_model

from event_calendar.models.youtube_music import YoutubeMusicEvent
from shared.models import TimeStampedModel

User = get_user_model()


class EventCalendar(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="calendar")
    youtube = models.ForeignKey(YoutubeMusicEvent, on_delete=models.CASCADE, related_name="yotubue", null=True)
    calendar_dt = models.DateField(help_text="캘린더 날짜")
    title = models.CharField(max_length=20, default="", help_text="이미지에 표현 될 메시지")
    comment = models.CharField(max_length=20, help_text="캘린더에 등록 될 메시지")
    is_shareable = models.BooleanField(default=False, help_text="캘린더 공유하기 여부")
    share_key = models.UUIDField(default=uuid.uuid4, editable=False, help_text="외부 사용자 접근 키")
    default_image = models.URLField(help_text="캘린더 기본 이미지")
    thumbnail_file = models.ImageField(
        upload_to="calendar_thumbnail", blank=True, null=True, help_text="캘린더 사용자 등록 이미지"
    )

    class Meta:
        app_label = "event_calendar"
        db_table = "event_calendar"
        (models.Index(fields=["is_shareable", "share_key"]),)
