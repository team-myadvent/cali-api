from django.apps import AppConfig


class EventCalendarConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "event_calendar"

    def ready(self):
        from event_calendar import signal  # noqa
