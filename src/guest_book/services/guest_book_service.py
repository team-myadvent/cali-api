from guest_book.exceptions import GuestBookEmptyContent, GuestBookEmptyWriterName


class GuestBookService:
    def __init__(self, model):
        self.model = model

    def create_guest_book(self, calendar, user, request):
        writer_name = request.data.get("writer_name")
        content = request.data.get("content")
        writer_ip = request.META.get("REMOTE_ADDR", "")

        if not content:
            raise GuestBookEmptyContent()

        if not request.user.is_authenticated:
            user = None

        if not writer_name and request.user.is_authenticated:
            writer_name = user.username

        if not writer_name:
            raise GuestBookEmptyWriterName()

        return self.model.objects.create(
            user=user,
            writer_name=writer_name,
            calendar=calendar,
            content=content,
            writer_ip=writer_ip,
        )
