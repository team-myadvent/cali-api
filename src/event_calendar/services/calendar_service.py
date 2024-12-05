from event_calendar.exceptions import ImageFileRequired
from event_calendar.models.share_image import ShareImage


class CalendarService:
    def __init__(self, model):
        self.model = model

    def get_event_calendar_by_calendar_id(self, calendar_id):
        try:
            return self.model.objects.get(id=calendar_id)
        except self.model.DoesNotExist:
            return None

    def get_event_calendar_all_for_request_user(self, user):
        queryset = self.model.objects.filter(user=user)

        if not queryset.exists():
            return None
        return queryset

    def get_event_calendar_all_by_public_key(self, calendar_id):
        queryset = self.model.objects.filter(is_shareable=True, share_key=calendar_id)

        if not queryset.exists():
            return None
        return queryset

    @staticmethod
    def create_event_calendar_share_image(request, calendar_dt=None):
        request_user = request.user
        image = request.data.get("export_image")

        if not image:
            raise ImageFileRequired()

        return ShareImage.objects.create(user=request_user, calendar_dt=calendar_dt, share_image=image)
