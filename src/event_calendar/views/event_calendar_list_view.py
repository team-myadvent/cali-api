from rest_framework.permissions import IsAuthenticatedOrReadOnly

from event_calendar.models import EventCalendar
from event_calendar.serializers.calendar_serializer import (
    CalendarListSerializer,
    CalendarCardSerializer,
)
from event_calendar.services.calendar_service import CalendarService
from shared.api import BaseAPIView
from user.exceptions import UserNotFound
from user.models import SocialUser


class EventCalendarListAPI(BaseAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    service = CalendarService(EventCalendar)

    def get_event_calendar(self, request=None, calendar_id=None):
        if calendar_id:
            return self.service.get_event_calendar_all_by_public_key(calendar_id)

        if request:
            return self.service.get_event_calendar_all_for_request_user(request.user)

    @staticmethod
    def get_user(user_id):
        try:
            return SocialUser.objects.get(social_id=user_id)
        except SocialUser.DoesNotExist:
            raise UserNotFound

    def get(self, request, user_id):
        user = self.get_user(user_id)
        calendar_card_id = request.query_params.get("idx")

        if calendar_card_id:
            calendar_card = self.service.get_event_calendar_by_calendar_id(user, calendar_card_id)
            calendar_serializer = CalendarCardSerializer(calendar_card)
            return self.success_response(
                data=calendar_serializer.data, message="Successfully retrieved event calendar card"
            )

        calendar = self.service.get_event_calendar_all_for_request_user(user)

        if not calendar:
            return self.fail_response(message=f"Does not found calendar. {user}`")

        calendar_serializer = CalendarListSerializer(calendar)

        return self.success_response(data=calendar_serializer.data, message="Successfully retrieved calendar")

    def post(self, request, user_id, *args, **kwargs):
        """
        캘린더 카드 데이터 이미지 저장하기
        """
        user = request.user
        share_image = request.data.get("export_image")

        if not share_image:
            return self.fail_response(message="Must be have export image")

        self.service.create_share_image(user, share_image)
        return self.success_response(message="Successfully created share_image")
