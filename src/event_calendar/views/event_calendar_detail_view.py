from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from event_calendar.exceptions import CalendarCardNotFound
from event_calendar.models import EventCalendar
from event_calendar.serializers.calendar_serializer import CalendarCardSerializer, UpdateCalendarCardSerializer
from event_calendar.services.calendar_service import CalendarService
from shared.api import BaseAPIView
from user.exceptions import UserNotFound
from user.models import SocialUser


class EventCalendarDetailAPI(BaseAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    service = CalendarService(EventCalendar)

    @staticmethod
    def get_user(user_id):
        try:
            return SocialUser.objects.get(social_id=user_id)
        except SocialUser.DoesNotExist:
            raise UserNotFound

    def get_object(self, user_id, calendar_id):
        user = self.get_user(user_id)
        calendar_card = self.service.get_event_calendar_by_calendar_id(user, calendar_id)

        if not calendar_card:
            raise CalendarCardNotFound

        return calendar_card

    def get(self, request, user_id, calendar_id, *args, **kwargs):
        """
        개별 캘린더 카드 접근
        """
        calendar_card = self.get_object(user_id, calendar_id)
        if not calendar_card:
            self.fail_response(message=f"Calendar card not found, id: `{calendar_id}`")

        calendar_serializer = CalendarCardSerializer(calendar_card)
        return self.success_response(
            data=calendar_serializer.data, message="Successfully retrieved event calendar card"
        )

    def put(self, request, user_id, calendar_id, *args, **kwargs):
        """
        개별 캘린더 카드 데이터 수정
        """
        calendar_card = self.get_object(user_id, calendar_id)
        if not calendar_card:
            self.fail_response(message=f"Calendar card not found, id: `{calendar_id}`")

        serializer = UpdateCalendarCardSerializer(calendar_card, data=request.data, partial=True)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except APIException as e:
            return self.fail_response(data=request.data, message=e.detail)

        return self.success_response(data=serializer.data, message="Successfully update profile")

    def post(self, request, user_id, calendar_id, *args, **kwargs):
        """
        캘린더 카드 데이터 이미지 저장하기
        """
        user = request.user
        share_image = request.data.get("export_image")

        if not share_image:
            return self.fail_response(message="Must be have export image")

        self.service.create_share_image(user, share_image)
        return self.success_response(message="Successfully created share_image")
