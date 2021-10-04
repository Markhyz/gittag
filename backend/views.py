from django.conf import settings

from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import requests
import github

from backend.models import RepositoryTag, GitHubUser
from backend.serializers import RepositoryTagSerializer
from backend.permissions import AuthenticatedUser, NoDuplicatedTag
from backend.utils import encode_jwt, get_current_user, GITHUB_OAUTH_ACCESS_TOKEN_URL


class RepositoryTagViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    serializer_class = RepositoryTagSerializer
    permission_classes = [AuthenticatedUser, NoDuplicatedTag]

    def get_queryset(self):
        return RepositoryTag.objects.filter(user_id=self.user_id)

    def perform_create(self, serializer):
        serializer.save(user_id=self.user_id)


class GitHubAuth(APIView):
    def post(self, request, format=None):
        github_oauth_code = request.data.get('code', None)
        if github_oauth_code is None:
            return Response({'message': 'Missing \'code\' parameter'}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            'client_id': settings.GITHUB_OAUTH_CLIENT_ID,
            'client_secret': settings.GITHUB_OAUTH_CLIENT_SECRET,
            'code': github_oauth_code}
        headers = {'Accept': 'application/json'}
        github_request_data = requests.post(
            GITHUB_OAUTH_ACCESS_TOKEN_URL, data=data, headers=headers).json()

        if 'error' in github_request_data:
            return Response({'message': github_request_data['error_description']}, status=status.HTTP_400_BAD_REQUEST)

        oauth_token = github_request_data.get('access_token', None)
        if oauth_token is None:
            return Response({'message': 'Failed to retrieve access token'}, status=status.HTTP_400_BAD_REQUEST)

        github_api = github.Github(oauth_token)
        try:
            user_id = github_api.get_user().id
        except github.GithubException as err:
            return Response({'message': err.data.message}, status=err.status)
        else:
            user = GitHubUser(user_id=user_id, oauth_token=oauth_token)
            user.save()
            access_token = encode_jwt({'user_id': user_id})
            return Response({'access_token': access_token})


@api_view(['GET'])
@permission_classes([AuthenticatedUser])
def get_github_user(request):
    access_token = request.headers['Authorization']
    user = get_current_user(access_token)
    github_api = github.Github(user.oauth_token)
    try:
        user_data = {'name': github_api.get_user().name,
                     'avatar_url': github_api.get_user().avatar_url}
    except github.GithubException as err:
        return Response({'message': err.data.message}, status=err.status)
    else:
        return Response(user_data)


@api_view(['GET'])
@permission_classes([AuthenticatedUser])
def get_github_user_starred(request):
    access_token = request.headers['Authorization']
    user = get_current_user(access_token)
    github_api = github.Github(user.oauth_token)
    try:
        starred_data = list(map(lambda repo: {
                            'id': repo.id,
                            'name': repo.full_name,
                            'description': repo.description,
                            'url': repo.html_url
                            }, github_api.get_user().get_starred()))
    except github.GithubException as err:
        return Response({'message': err.data.message}, status=err.status)
    else:
        return Response(starred_data)
