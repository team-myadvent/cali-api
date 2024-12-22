from profiles.exceptions import CouldNotFoundProfile


class ProfileService:
    def __init__(self, model):
        self.model = model

    @property
    def select_related(self):
        return self.model.objects.select_related("user").all()

    def get_profile_by_user(self, user):
        try:
            return self.select_related.get(user=user)
        except self.model.DoesNotExist:
            raise CouldNotFoundProfile(user)

    def get_profile_by_profile_id(self, profile_id):
        try:
            return self.model.objects.get(id=profile_id)
        except self.model.DoesNotExist:
            raise CouldNotFoundProfile(profile_id)
