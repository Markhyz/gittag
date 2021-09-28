from rest_framework import permissions

from backend.utils import decode_jwt


class AuthenticatedUser(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            access_token = request.headers['Authorization']
            data = decode_jwt(access_token)
            view.user_id = data['user_id']
        except:
            return False
        return True
