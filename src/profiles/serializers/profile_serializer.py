from django.db import IntegrityError
from rest_framework import serializers

from profiles.exceptions import AlreadyUseUserNameError
from profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="user.username")
    user_id = serializers.CharField(source="user.social_id")
    profile_id = serializers.CharField(source="id")
    profile_photo = serializers.SerializerMethodField()

    @staticmethod
    def get_profile_photo(obj):
        if obj.profile_photo_file:
            return obj.profile_photo_file.url

        if obj.profile_photo_url:
            return obj.profile_photo_url

    class Meta:
        model = Profile
        fields = [
            "profile_id",
            "user_id",
            "name",
            "profile_photo",
        ]


class UpdateProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", required=False)

    class Meta:
        model = Profile
        fields = [
            "username",
            "profile_photo_file",
        ]

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        username = user_data.get("username")
        profile_photo_file = validated_data.get("profile_photo_file")

        if profile_photo_file:
            instance.profile_photo_file = profile_photo_file

        if username and username != instance.user.username:
            instance.user.username = username
            try:
                instance.user.save()
            except IntegrityError:
                raise AlreadyUseUserNameError()

        instance.save()
        return instance
