from rest_framework import serializers

from event_calendar.models import EventCalendar


class CalendarCardSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source="user.id", read_only=True)
    youtube_music_link = serializers.URLField(source="youtube.music_url", read_only=False)
    calendar_thumbnail = serializers.SerializerMethodField()

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
            "title",
            "comment",
            "comment_detail",
            "youtube_music_link",
            "calendar_thumbnail",
        ]


class CalendarListSerializer(serializers.ListSerializer):
    child = CalendarCardSerializer()


class UpdateCalendarCardSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source="user.id", read_only=True)
    youtube_video_id = serializers.CharField(source="youtube.video_id")
    youtube_music_link = serializers.URLField(source="youtube.music_url")
    youtubue_thumbnail_link = serializers.URLField(source="youtube.thumbnail_url", write_only=True)
    calendar_thumbnail = serializers.SerializerMethodField()
    thumbnail_file = serializers.ImageField(use_url=True, write_only=True)

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
        youtube_music = youtube_data.get("music_url")

        thumbnail_file = validated_data.get("thumbnail_file")

        if youtube_music or youtube_thumbnail:
            if youtube_music != instance.youtube.music_url:
                instance.youtube.music_url = youtube_music

            if youtube_thumbnail != instance.youtube.thumbnail_url:
                instance.youtube.thumbnail_url = youtube_thumbnail

            instance.youtube.save()

        if thumbnail_file:
            instance.thumbnail_file = thumbnail_file

        for attr, value in validated_data.items():
            if attr not in ["youtube_thumbnail", "youtube_music", "thumbnail_file"]:
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
            "youtube_music_link",
            "youtubue_thumbnail_link",
            "calendar_thumbnail",
            "thumbnail_file",
        ]
