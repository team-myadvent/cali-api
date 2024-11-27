from django.db import models

from profiles.models.notification import Notification
from shared.models import TimeStampedModel
from user.models import SocialUser


class Profile(TimeStampedModel):
    user = models.OneToOneField(SocialUser, on_delete=models.CASCADE, related_name="profile")
    notification = models.OneToOneField(Notification, on_delete=models.CASCADE, related_name="notification")
    profile_photo = models.ImageField(upload_to="profile_photo")

    class Meta:
        app_label = "profiles"
        db_table = "user_profile"
        constraints = [
            models.UniqueConstraint(fields=["user"], name="user foreign key"),
        ]
