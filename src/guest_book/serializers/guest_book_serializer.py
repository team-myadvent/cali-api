from rest_framework import serializers

from guest_book.models import GuestBook


class GuestBookSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    userid = serializers.CharField(source="user.social_id", read_only=True)

    class Meta:
        model = GuestBook
        fields = [
            "username",
            "userid",
            "writer_name",
            "content",
        ]
