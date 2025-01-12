from django.http import HttpRequest
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

"""スタッフ権限か確認する"""
class IsAdmin(IsAuthenticated):
    def has_permission(self, request: HttpRequest, view: APIView) -> bool:
        if request.user.is_staff:
            return True
        return False