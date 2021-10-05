from rest_framework import permissions

from backend.utils import decode_jwt

from backend.models import RepositoryTag


class AuthenticatedUser(permissions.BasePermission):
    def has_permission(self, request, view):
        """
        A user is authenticated if the access token is valid
        """
        try:
            access_token = request.headers['Authorization']
            data = decode_jwt(access_token)
            view.user_id = data['user_id']
        except:
            return False
        return True


class NoDuplicatedTag(permissions.BasePermission):
    def has_permission(self, request, view):
        """
        Prohibits the duplication of tags (same user, repository and tag name)
        """
        try:
            view.get_queryset().get(name=request.data.get("name", None),
                                    repository_id=request.data.get("repository_id", None))
            return False
        except RepositoryTag.DoesNotExist:
            return True
