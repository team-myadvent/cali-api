import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from config.django.base import AUTH_USER_MODEL
from event_calendar.models import EventCalendar

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_calendar(sender, instance, created, **kwagrs):
    logger.debug("user default calendar creating...")

    queryset = EventCalendar.objects.filter(user=None)

    if created:
        for data in queryset:
            EventCalendar.objects.create(
                user=instance,
                youtube=data.youtube,
                calendar_dt=data.calendar_dt,
                seq_no=data.seq_no,
                title=data.title,
                comment=data.comment,
                comment_detail=data.comment_detail,
                default_image=data.default_image,
            )
