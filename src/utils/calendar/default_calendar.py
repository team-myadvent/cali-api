import random

from datetime import date

from config.settings.storages import S3_IMAGE_URL

TODAY = date.today()
MONTH = 12
MAX_DAYS = 26
YEAR = TODAY.year

SEQ_VALUES = list(range(1, MAX_DAYS))
random.shuffle(SEQ_VALUES)


def get_default_calendar_data():
    default_data = []

    for day, seq in zip(range(1, MAX_DAYS), SEQ_VALUES):
        current_date = date(YEAR, MONTH, day)

        default_data.append(
            {
                "calendar_dt": current_date,
                "title": f"{current_date}",
                "comment": f"{current_date}",
                "comment_detail": "",
                "youtube_music_link": None,
                "default_image": S3_IMAGE_URL.format(seq=seq),
            }
        )
    return default_data
