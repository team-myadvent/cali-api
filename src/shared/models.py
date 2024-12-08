from django.db import models


class TimeStampedModel(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = [
            "-created_at",
            "-updated_at",
        ]
