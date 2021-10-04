from types import SimpleNamespace
from unittest.mock import patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from backend.models import GitHubUser
from backend.tests.constants import TEST_USER_ID, TEST_ACCESS_TOKEN


@patch('backend.views.github.Github')
class GithubProxyTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        GitHubUser.objects.create(
            user_id=TEST_USER_ID,
            oauth_token=TEST_ACCESS_TOKEN
        )

    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION=TEST_ACCESS_TOKEN)

    def test_get_github_user(self, mock_github_api):
        user_name = 'bob'
        avatar_url = 'www.example.com'

        mock_github_api.return_value.get_user.return_value.name = user_name
        mock_github_api.return_value.get_user.return_value.avatar_url = avatar_url

        url = reverse('github-user')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], user_name)
        self.assertEqual(response.data['avatar_url'], avatar_url)

    def test_get_github_starred(self, mock_github_api):
        number_of_starred_repositories = 7
        starred_repositories = [
            {
                'id': starred_repository_id,
                'name': f'test-{starred_repository_id}',
                'description': f'This is test repository number {starred_repository_id}',
                'url': f'www.example.com/{starred_repository_id}'
            }
            for starred_repository_id in range(number_of_starred_repositories)
        ]
        starred_repositories_as_objects = map(
            lambda repository: SimpleNamespace(
                id=repository['id'],
                full_name=repository['name'],
                description=repository['description'],
                html_url=repository['url']
            ),
            starred_repositories
        )

        mock_github_api.return_value.get_user.return_value.get_starred.return_value = starred_repositories_as_objects

        url = reverse('github-starred')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, starred_repositories)
