from django.db import models
from django.contrib.auth import get_user_model

from shared.models import TimeStampedModel


User = get_user_model()


class YoutubeMusicEvent(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="youtube_music")
    music_url = models.URLField(max_length=255, null=True, blank=True)
    thumbnail_url = models.URLField(max_length=255, null=True, blank=True)

    class Meta:
        app_label = "event_calendar"
        db_table = "youtube_music"
