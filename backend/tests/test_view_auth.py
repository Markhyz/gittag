from unittest.mock import patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from backend.tests.constants import TEST_USER_ID, TEST_ACCESS_TOKEN


@patch('backend.views.github.Github')
class AuthTests(APITestCase):
    @patch('backend.views.requests.post')
    def test_auth(self, mock_post, mock_github_api):
        mock_post.return_value.json.return_value = {
            'access_token': TEST_ACCESS_TOKEN
        }
        mock_github_api.return_value.get_user.return_value.id = TEST_USER_ID

        url = reverse('auth')
        data = {'code': 'code'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['access_token'], TEST_ACCESS_TOKEN)
