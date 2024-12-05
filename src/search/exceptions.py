from rest_framework.exceptions import APIException


class SearchResponseEmtpy(APIException):
    status_code = 400
    default_detail = "Search response has empty"
