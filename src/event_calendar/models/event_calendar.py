from django.db import models
from django.contrib.auth import get_user_model

from event_calendar.models.youtube_music import YoutubeMusicEvent
from shared.models import TimeStampedModel

User = get_user_model()


class EventCalendar(TimeStampedModel):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name="calendar")
    youtube = models.ForeignKey(YoutubeMusicEvent, on_delete=models.CASCADE, related_name="yotubue", null=True)
    calendar_dt = models.DateField(help_text="캘린더 날짜")
    seq_no = models.IntegerField(default=0, help_text="캘린더 인덱스 번호")
    title = models.CharField(max_length=255, default="", help_text="유튜브 음악 제목")
    comment = models.CharField(max_length=100, default="", help_text="이미지 표현 될 메시지")
    comment_detail = models.TextField(default="", null=True, blank=True, help_text="캘린더 메시지")
    default_image = models.URLField(help_text="캘린더 기본 이미지")
    thumbnail_file = models.ImageField(
        upload_to="calendar_thumbnail", blank=True, null=True, help_text="캘린더 사용자 등록 이미지"
    )

    class Meta:
        app_label = "event_calendar"
        db_table = "event_calendar"
        ordering = ["calendar_dt", "seq_no"]
