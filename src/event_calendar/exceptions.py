from rest_framework.exceptions import APIException


class CalendarCardNotFound(APIException):
    status_code = 400
    default_detail = "Does not found calendar card"
