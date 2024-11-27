from datetime import time
from django.db import models
from shared.models import TimeStampedModel


class Notification(TimeStampedModel):
    is_enabled = models.BooleanField(default=False, help_text="알림 활성화 여부")
    notification_dtm = models.TimeField(default=time(8, 0))

    class Meta:
        app_label = "profiles"
        db_table = "notifications"
