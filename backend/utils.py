from django.conf import settings

import jwt

from backend.models import GitHubUser

GITHUB_OAUTH_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'


def encode_jwt(data):
    """
    Generates encoded JWT token
    """
    return jwt.encode(data, settings.SECRET_KEY, algorithm='HS256')


def decode_jwt(data):
    """
    Decodes JWT token
    """
    return jwt.decode(data, settings.SECRET_KEY, algorithms='HS256')


def get_current_user(access_token):
    """
    Retrieves the authenticated user 
    """
    user_id = decode_jwt(access_token)['user_id']
    return GitHubUser.objects.get(user_id=user_id)
