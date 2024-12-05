from rest_framework.exceptions import APIException


class ImageFileRequired(APIException):
    status_code = 400
    default_detail = "Required image file"
