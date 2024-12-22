from rest_framework.exceptions import APIException


class GuestBookEmptyContent(APIException):
    status_code = 400
    default_detail = "Must be have guest book content"


class GuestBookEmptyWriterName(APIException):
    status_code = 400
    default_detail = "Must be have guest book writer name"
