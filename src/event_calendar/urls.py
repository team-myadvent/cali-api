from django.urls import path

from event_calendar import views


urlpatterns = [
    path("", views.EventCalendarDefaultAPI.as_view(), name="default-calendar-list"),
    path("/<int:user_id>", views.EventCalendarListAPI.as_view(), name="calendar-list"),
    path(
        "/card/<int:user_id>/<int:calendar_id>",
        views.EventCalendarDetailAPI.as_view(),
        name="calendar-card",
    ),
]
