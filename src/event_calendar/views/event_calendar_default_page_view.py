from rest_framework.permissions import AllowAny

from event_calendar.models import EventCalendar
from event_calendar.services.calendar_service import CalendarService
from shared.api import BaseAPIView
from utils.calendar.default_calendar import get_default_calendar_data


class EventCalendarDefaultAPI(BaseAPIView):
    permission_classes = [AllowAny]
    service = CalendarService(EventCalendar)

    def get(self, request):
        query_param = request.query_params.get("idx")
        default_data = get_default_calendar_data()

        if query_param:
            try:
                default_data = default_data[int(query_param) - 1]
                return self.success_response(data=default_data, message="Successfully retrieved calendar")
            except IndexError:
                return self.fail_response(message="Does not have calendar idx")

        return self.success_response(data=default_data, message="Successfully retrieved calendar")
