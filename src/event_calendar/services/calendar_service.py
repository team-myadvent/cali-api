from event_calendar.exceptions import CalendarCardNotFound
from event_calendar.models import ShareImage


class CalendarService:
    def __init__(self, model):
        self.model = model

    def get_event_calendar_by_calendar_id(self, user, calendar_id):
        try:
            return self.model.objects.get(user=user, id=calendar_id)
        except self.model.DoesNotExist:
            raise CalendarCardNotFound

    def get_event_calendar_all_for_request_user(self, user):
        queryset = self.model.objects.filter(user=user)

        if not queryset.exists():
            return None
        return queryset

    def get_event_calendar_all_by_public_key(self, share_key):
        queryset = self.model.objects.filter(is_shareable=True, share_key=share_key)

        if not queryset.exists():
            return None
        return queryset

    def get_event_calendar_detail_by_public_key_seq_no(self, share_key, seq_no):
        try:
            return self.model.objects.get(is_shareable=True, share_key=share_key, seq_no=seq_no)
            # return self.model.objects.get(share_key=share_key, seq_no=seq_no)
        except self.model.DoesNotExist:
            return None

    @staticmethod
    def create_share_image(user, share_image):
        return ShareImage.objects.create(user=user, share_image=share_image)
