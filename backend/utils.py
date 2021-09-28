from django.conf import settings

import jwt

from backend.models import GitHubUser


def encode_jwt(data):
    return jwt.encode(data, settings.SECRET_KEY, algorithm='HS256')


def decode_jwt(data):
    return jwt.decode(data, settings.SECRET_KEY, algorithms='HS256')


def get_current_user(access_token):
    user_id = decode_jwt(access_token)['user_id']
    return GitHubUser.objects.get(user_id=user_id)
