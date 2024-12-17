from django.contrib.auth import get_user_model

from user.exceptions import UserNotFound

User = get_user_model()


class UserService:
    @staticmethod
    def get_user_by_social_id(social_id):
        try:
            return User.objects.get(social_id=social_id)
        except User.DoesNotExist:
            raise UserNotFound()
