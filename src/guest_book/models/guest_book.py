from django.contrib.auth import get_user_model
from django.db import models
from shared.models import TimeStampedModel


User = get_user_model()


class GuestBook(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="guestbooks", null=True, blank=True)
    writer_name = models.CharField(max_length=20, null=True, blank=True)
    calendar = models.ForeignKey("event_calendar.EventCalendar", on_delete=models.CASCADE, related_name="guestbooks")
    content = models.TextField(help_text="방명록 내용")
    writer_ip = models.GenericIPAddressField(null=True, blank=True, help_text="작성자 IP 주소")

    class Meta:
        app_label = "guest_book"
        db_table = "guest_book"
        ordering = ["created_at"]
