from django.urls import path

from profiles.views import views


urlpatterns = [
    path(
        "/<str:profile_id>",
        views.UserProfileDetailAPI.as_view(),
        name="user-profile",
    ),
]
