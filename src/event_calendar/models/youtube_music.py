from django.db import models
from django.contrib.auth import get_user_model

from shared.models import TimeStampedModel


User = get_user_model()


class YoutubeMusicEvent(TimeStampedModel):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name="youtube_music")
    video_id = models.CharField(max_length=100, null=True, blank=True, help_text="유튜브 비디오 아이디")
    thumbnail_url = models.URLField(max_length=255, null=True, blank=True, help_text="유튜브 섬네일 링크")

    class Meta:
        app_label = "event_calendar"
        db_table = "youtube_music"
