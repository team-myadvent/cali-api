from django.urls import path

from event_calendar.views import views


urlpatterns = [
    path("", views.EventCalendarListAPI.as_view(), name="calendar-list"),
    path("/share", views.EventCalendarShareAPI.as_view(), name="share-user-calendar-list"),
    path("/share/<str:share_key>", views.EventCalendarShareAPI.as_view(), name="share-user-calendar-list"),
    path(
        "/card/<uuid:calendar_id>",
        views.EventCalendarDetailAPI.as_view(),
        name="calendar-card",
    ),
]
