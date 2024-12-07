import logging
import random
from datetime import date

from django.db.models.signals import post_save
from django.dispatch import receiver


from config.django.base import AUTH_USER_MODEL
from config.settings.storages import S3_IMAGE_URL
from event_calendar.models import EventCalendar, YoutubeMusicEvent

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_calendar(sender, instance, created, **kwagrs):
    logger.debug("user default calendar creating...")

    today = date.today()
    month = 12
    max_days = 26
    year = today.year

    seq_values = list(range(1, max_days))
    random.shuffle(seq_values)

    if created:
        for day, seq in zip(range(1, max_days), seq_values):
            current_date = date(year, month, day)

            EventCalendar.objects.create(
                user=instance,
                youtube=YoutubeMusicEvent.objects.create(user=instance),
                calendar_dt=current_date,
                seq_no=day,
                title=f"{current_date}",
                comment=f"{current_date}",
                comment_detail="",
                default_image=S3_IMAGE_URL.format(seq=seq),
            )
