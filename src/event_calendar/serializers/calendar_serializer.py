from rest_framework import serializers

from event_calendar.models import EventCalendar
from guest_book.serializers.guest_book_serializer import GuestBookSerializer
from utils.event_calendar.youtube_thumbnail_image import get_youtube_thumbnail_image_size


class CalendarCardSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source="user.id", read_only=True)
    youtube_video_id = serializers.URLField(source="youtube.video_id", read_only=True)
    calendar_thumbnail = serializers.SerializerMethodField()
    guestbooks = GuestBookSerializer(many=True, read_only=True)

    @staticmethod
    def get_calendar_thumbnail(obj):
        # 썸네일 파일과 유튜브 썸네일의 최근 업데이트 시간 비교
        thumbnail_updated = obj.updated_at and obj.thumbnail_file
        youtube_updated = obj.youtube.thumbnail_url and obj.youtube.updated_at

        if thumbnail_updated and youtube_updated:
            if obj.updated_at > obj.youtube.updated_at:
                return obj.thumbnail_file.url
            else:
                return obj.youtube.thumbnail_url

        # NOTE: 사용자가 새로운 이미지를 등록했다면 항상 사용자 등록 이미지
        if obj.thumbnail_file:
            return obj.thumbnail_file.url

        # NOTE: 유튜브 음악이 등록되어 있고, 새 이미지가 없다면 유튜브 썸네일
        if obj.youtube.thumbnail_url and not obj.thumbnail_file:
            return obj.youtube.thumbnail_url

        # NOTE: 그 외 모든 조건은 기본 이미지
        return obj.default_image

    class Meta:
        model = EventCalendar
        fields = [
            "id",
            "user_id",
            "calendar_dt",
            "guestbooks",
            "title",
            "comment",
            "comment_detail",
            "youtube_video_id",
            "calendar_thumbnail",
            "thumbnail_file",
        ]


class CalendarListSerializer(serializers.ListSerializer):
    child = CalendarCardSerializer()


class UpdateCalendarCardSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source="user.id", read_only=True)
    youtube_video_id = serializers.CharField(source="youtube.video_id", allow_null=True, allow_blank=True)
    youtube_thumbnail_link = serializers.URLField(source="youtube.thumbnail_url", write_only=True)
    calendar_thumbnail = serializers.SerializerMethodField()
    thumbnail_file = serializers.ImageField(allow_null=True, required=False, use_url=True, write_only=True)

    @staticmethod
    def get_calendar_thumbnail(obj):
        # 썸네일 파일과 유튜브 썸네일의 최근 업데이트 시간 비교
        thumbnail_updated = obj.updated_at and obj.thumbnail_file
        youtube_updated = obj.youtube.thumbnail_url and obj.youtube.updated_at

        if thumbnail_updated and youtube_updated:
            if obj.updated_at > obj.youtube.updated_at:
                return obj.thumbnail_file.url
            else:
                return obj.youtube.thumbnail_url

        # NOTE: 사용자가 새로운 이미지를 등록했다면 항상 사용자 등록 이미지
        if obj.thumbnail_file:
            return obj.thumbnail_file.url

        # NOTE: 유튜브 음악이 등록되어 있고, 새 이미지가 없다면 유튜브 썸네일
        if obj.youtube.thumbnail_url and not obj.thumbnail_file:
            return obj.youtube.thumbnail_url

        # NOTE: 그 외 모든 조건은 기본 이미지
        return obj.default_image

    def update(self, instance, validated_data):
        youtube_data = validated_data.pop("youtube", {})
        youtube_thumbnail = youtube_data.get("thumbnail_url")
        youtube_video_id = youtube_data.get("video_id")

        thumbnail_file = validated_data.get("thumbnail_file")

        # NOTE: 유튜브 썸네일 이미지를 입력 하였거나 유튜브 비디오 아이디를 입력 한 경우
        if youtube_thumbnail or youtube_video_id:
            if youtube_thumbnail != instance.youtube.thumbnail_url and youtube_thumbnail:
                youtube_thumbnail_size = get_youtube_thumbnail_image_size(youtube_thumbnail)

                # NOTE: default thumbnail size가 120, 90 일 때 저장 하지 않음
                if youtube_thumbnail_size.is_invalid_image_size():
                    youtube_thumbnail = youtube_thumbnail.replace("maxresdefault", "hqdefault")

                instance.youtube.thumbnail_url = youtube_thumbnail
            if youtube_video_id != instance.youtube.video_id and youtube_video_id:
                instance.youtube.video_id = youtube_video_id

            instance.youtube.save()

        instance.thumbnail_file = thumbnail_file

        for attr, value in validated_data.items():
            if attr not in ["youtube_thumbnail", "thumbnail_file"]:
                setattr(instance, attr, value)

        instance.save()
        return instance

    class Meta:
        model = EventCalendar
        fields = [
            "id",
            "user_id",
            "calendar_dt",
            "title",
            "comment",
            "comment_detail",
            "youtube_video_id",
            "youtube_thumbnail_link",
            "calendar_thumbnail",
            "thumbnail_file",
        ]
