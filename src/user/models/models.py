from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class SocialUser(AbstractBaseUser):
    pkid = models.BigAutoField(primary_key=True, editable=False, help_text="고유 아이디")
    social_id = models.CharField(max_length=100, unique=True, help_text="유저 플랫폼 고유 아이디")
    username = models.CharField(max_length=50, unique=True, help_text="플랫폼 유저 이름")
    age_range = models.CharField(max_length=50, help_text="유저 연령대")
    birthday = models.CharField(max_length=50, help_text="생일 일자")
    email = models.CharField(max_length=50, help_text="유저 플랫폼 가입 이메일")
    platform = models.CharField(max_length=50, help_text="플랫폼 명칭")
    profile_image = models.CharField(max_length=255, help_text="프로필 이미지 사진 URL")
    is_active = models.BooleanField(default=True, help_text="유저 활성화 여부")
    last_login = models.DateTimeField(auto_now=True, help_text="마지막 로그인 일자")
    created_at = models.DateTimeField(auto_now_add=True, help_text="최초 가입 일자")

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["social_id", "platform"]

    class Meta:
        app_label = "user"
        db_table = "service_user"
        constraints = [
            models.UniqueConstraint(fields=["social_id"], name="unique_social_id"),
        ]

    def __str__(self):
        return self.social_id
