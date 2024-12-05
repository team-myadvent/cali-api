import uuid

from django.db import models
from django.contrib.auth import get_user_model

from shared.models import TimeStampedModel

User = get_user_model()


class ShareImage(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="share_image")
    calendar_dt = models.DateField(null=True, blank=True, help_text="캘린더 날짜")
    share_image = models.ImageField(upload_to="share_image", help_text="사용자 공유 이미지")

    class Meta:
        app_label = "event_calendar"
        db_table = "share_image"
