from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_201_CREATED

from event_calendar.models import EventCalendar
from event_calendar.services.calendar_service import CalendarService
from guest_book.models import GuestBook
from guest_book.services.guest_book_service import GuestBookService
from shared.api import BaseAPIView
from user.services.user_service import UserService

User = get_user_model()


class GuestBookAPI(BaseAPIView):
    permission_classes = [AllowAny]
    service = GuestBookService(GuestBook)
    calendar_service = CalendarService(EventCalendar)

    def post(self, request, social_id, calendar_id, *args, **kwargs):
        user = UserService.get_user_by_social_id(social_id)
        calendar = self.calendar_service.get_event_calendar_by_calendar_id(user, calendar_id)

        self.service.create_guest_book(calendar, user, request)
        return self.success_response(message="Successfully created guest book", status_code=HTTP_201_CREATED)
