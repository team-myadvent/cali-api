from django.utils.functional import classproperty

from profiles.exceptions import CouldNotFoundProfile
from profiles.models import Profile


class ProfileService:
    @classproperty
    def select_related(self):
        return Profile.objects.select_related("user").all()

    @staticmethod
    def get_profile_by_profile_id(profile_id) -> Profile:
        try:
            return Profile.objects.get(id=profile_id)
        except Profile.DoesNotExist:
            raise CouldNotFoundProfile(profile_id)
