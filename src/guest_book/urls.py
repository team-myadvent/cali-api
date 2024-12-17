from django.urls import path

from guest_book import views


urlpatterns = [path("/<int:social_id>/<int:calendar_id>", views.GuestBookAPI.as_view(), name="create-guest-book")]
