from rest_framework.exceptions import APIException


class DataNotFoundException(APIException):
    status_code = 404
    default_detail = "閲覧する権限がありません"
    default_code = "permission_denied"