from rest_framework.exceptions import APIException


class CouldNotFoundProfile(APIException):
    status_code = 400

    def __init__(self, info):
        self.detail = f"`{info}` could not be found into profiles"


class AlreadyUseUserNameError(APIException):
    status_code = 400
    default_detail = "Username already used."
