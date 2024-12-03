from django.conf import settings

from rest_framework.exceptions import APIException
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from event_calendar.models import EventCalendar
from event_calendar.serializers.calendar_serializer import (
    CalendarCardSerializer,
    CalendarListSerializer,
    UpdateCalendarCardSerializer,
)
from event_calendar.services.calendar_service import CalendarService
from shared.api import BaseAPIView


class EventCalendarDetailAPI(BaseAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    service = CalendarService(EventCalendar)

    def get(self, request, calendar_id, *args, **kwargs):
        calendar_card = self.service.get_event_calendar_by_calendar_id(calendar_id)

        if not calendar_card:
            return self.fail_response(message=f"Does not found calendar card, id: `{calendar_id}`")

        calendar_serializer = CalendarCardSerializer(calendar_card)
        return self.success_response(
            data=calendar_serializer.data, message="Successfully retrieved event calendar card"
        )

    def put(self, request, calendar_id, *args, **kwargs):
        calendar_card = self.service.get_event_calendar_by_calendar_id(calendar_id)

        if not calendar_card:
            return self.fail_response(message=f"Does not found calendar card, id: `{calendar_id}`")

        serializer = UpdateCalendarCardSerializer(calendar_card, data=request.data, partial=True)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except APIException as e:
            return self.fail_response(data=request.data, message=e.detail)

        return self.success_response(data=serializer.data, message="Successfully update profile")


class EventCalendarListAPI(BaseAPIView):
    service = CalendarService(EventCalendar)

    def get_event_calendar(self, request=None, calendar_id=None):
        if calendar_id:
            return self.service.get_event_calendar_all_by_public_key(calendar_id)

        if request:
            return self.service.get_event_calendar_all_for_request_user(request.user)

    def get(self, request):
        calendar = self.service.get_event_calendar_all_for_request_user(request.user)

        if not calendar:
            return self.fail_response(message=f"Does not found calendar. {request.user}`")

        calendar_serializer = CalendarListSerializer(calendar)

        return self.success_response(data=calendar_serializer.data, message="Successfully retrieved calendar")


class EventCalendarShareAPI(BaseAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    service = CalendarService(EventCalendar)

    def get(self, request, share_key):
        calendar = self.service.get_event_calendar_all_by_public_key(share_key)

        if not calendar:
            return self.fail_response(message=f"Does not found calendar id or has not shared, id: `{share_key}`")

        calendar_serializer = CalendarListSerializer(calendar)

        return self.success_response(data=calendar_serializer.data, message="Successfully retrieved calendar")

    def post(self, request):
        calendars = self.service.get_event_calendar_all_for_request_user(request.user)

        for calendar in calendars:
            calendar.is_shareable = True
            calendar.save()

        if calendars:
            first_calendar = calendars.first()

            return self.success_response(
                data={"share_link": f"{settings.DOMAIN}/api/v1/calendars/share/{first_calendar.share_key}"},
                message="Successfully shared all calendars",
            )

        return self.fail_response(message="No calendars found to share")
