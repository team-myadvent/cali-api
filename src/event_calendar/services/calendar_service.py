from event_calendar.exceptions import CalendarCardNotFound
from event_calendar.models import ShareImage


class CalendarService:
    def __init__(self, model):
        self.model = model

    def get_event_calendar_by_calendar_id(self, user, calendar_id):
        calendar_card = (
            self.model.objects.select_related("user", "youtube").filter(user=user, seq_no=calendar_id).first()
        )

        if not calendar_card:
            raise CalendarCardNotFound()
        return calendar_card

    def get_event_calendar_all_for_request_user(self, user):
        queryset = self.model.objects.select_related("user", "youtube").prefetch_related("guestbooks").filter(user=user)
        calendar_list = list(queryset)

        if not calendar_list:
            return None

        return calendar_list

    @staticmethod
    def create_share_image(user, share_image):
        return ShareImage.objects.create(user=user, share_image=share_image)
