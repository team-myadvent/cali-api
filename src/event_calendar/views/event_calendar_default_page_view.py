from rest_framework.permissions import AllowAny

from event_calendar.models import EventCalendar
from event_calendar.serializers.calendar_serializer import CalendarListSerializer, CalendarCardSerializer
from event_calendar.services.calendar_service import CalendarService
from shared.api import BaseAPIView


class EventCalendarDefaultAPI(BaseAPIView):
    permission_classes = [AllowAny]
    service = CalendarService(EventCalendar)

    def get(self, request):
        query_param = request.query_params.get("idx")

        if query_param:
            calendar_card = self.service.get_event_calendar_by_calendar_id(user=None, calendar_id=query_param)
            calendar_serializer = CalendarCardSerializer(calendar_card)
            return self.success_response(
                data=calendar_serializer.data, message="Successfully retrieved event calendar card"
            )

        default_calendar = self.service.get_event_calendar_all_for_request_user(user=None)
        calendar_serializer = CalendarListSerializer(default_calendar)
        return self.success_response(data=calendar_serializer.data, message="Successfully retrieved calendar")
