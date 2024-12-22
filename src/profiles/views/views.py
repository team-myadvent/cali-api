from rest_framework.exceptions import APIException
from rest_framework.request import Request

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from profiles.models import Profile
from profiles.serializers.profile_serializer import ProfileSerializer, UpdateProfileSerializer
from profiles.services.profile_service import ProfileService
from shared.api import BaseAPIView


class MyProfileAPI(BaseAPIView):
    profile_service = ProfileService(Profile)

    def get(self, request, *args, **kwargs):
        user = self.request.user

        profile = self.profile_service.get_profile_by_user(user=user)
        serializer = ProfileSerializer(profile)
        return self.success_response(data=serializer.data, message="Profile successfully retrieved")

    def put(self, request) -> Response:
        user = self.request.user
        profile = self.profile_service.get_profile_by_user(user=user)

        serializer: UpdateProfileSerializer = UpdateProfileSerializer(profile, data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except APIException as e:
            return self.fail_response(data=request.data, message=e.detail)

        return self.success_response(data=serializer.data, message="Successfully update profile")


class UserProfileDetailAPI(BaseAPIView):
    permission_classes = [AllowAny]
    profile_service = ProfileService(Profile)

    def get(self, request: Request, profile_id: str) -> Response:
        profile: Profile = self.profile_service.get_profile_by_profile_id(profile_id)
        serializer: ProfileSerializer = ProfileSerializer(profile)
        return self.success_response(
            data=serializer.data, message=f"{profile.user.username}'s profile successfully retrieved"
        )
