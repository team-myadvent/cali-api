from django.db import IntegrityError
from rest_framework import serializers

from profiles.exceptions import AlreadyUseUserNameError
from profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    user_id = serializers.CharField(source="user.social_id")
    profile_id = serializers.CharField(source="id")
    is_notification_enable = serializers.BooleanField(source="notification.is_enabled")
    notification_time = serializers.TimeField(source="notification.notification_dtm")
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
            "username",
            "profile_photo",
            "is_notification_enable",
            "notification_time",
        ]


class UpdateProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", required=False)
    is_notification_enable = serializers.BooleanField(source="notification.is_enabled", required=False)
    notification_time = serializers.TimeField(source="notification.notification_dtm", required=False)
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
            "username",
            "profile_photo",
            "is_notification_enable",
            "notification_time",
        ]

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        notification_data = validated_data.pop("notification", {})
        username = user_data.get("username")
        profile_photo_file = validated_data.get("profile_photo_file")
        is_notification_enable = notification_data.get("is_enabled")
        notification_time = notification_data.get("notification_dtm")

        if profile_photo_file:
            instance.profile_photo_file = profile_photo_file

        if username and username != instance.user.username:
            instance.user.username = username
            try:
                instance.user.save()
            except IntegrityError:
                raise AlreadyUseUserNameError()

        if is_notification_enable or notification_time:
            instance.notification.is_enabled = is_notification_enable
            instance.notification.notification_dtm = notification_time
            instance.notification.save()

        instance.save()
        return instance
