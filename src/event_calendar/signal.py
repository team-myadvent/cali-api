import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from config.django.base import AUTH_USER_MODEL
from event_calendar.models import EventCalendar, YoutubeMusicEvent

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_calendar(sender, instance, created, **kwagrs):
    logger.debug("user default calendar creating...")

    calendar_queryset = EventCalendar.objects.filter(user=None)

    if created:
        for data in calendar_queryset:
            youtube = YoutubeMusicEvent.objects.create(
                user=instance,
                video_id=data.youtube.video_id,
                thumbnail_url=data.youtube.thumbnail_url,
            )

            EventCalendar.objects.create(
                user=instance,
                youtube=youtube,
                calendar_dt=data.calendar_dt,
                seq_no=data.seq_no,
                title=data.title,
                comment=data.comment,
                comment_detail=data.comment_detail,
                default_image=data.default_image,
            )
