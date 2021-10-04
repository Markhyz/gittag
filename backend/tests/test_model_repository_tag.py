from backend.tests.test_proxy_github import TEST_ACCESS_TOKEN
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from backend.models import RepositoryTag
from backend.tests.constants import TEST_USER_ID, TEST_REPOSITORY_ID, TEST_TAG_NAME, TEST_ACCESS_TOKEN


def create_tag(user_id=TEST_USER_ID, repository_id=TEST_REPOSITORY_ID, tag_name=TEST_TAG_NAME):
    RepositoryTag.objects.create(
        user_id=user_id,
        repository_id=repository_id,
        name=tag_name
    )


def create_list_of_tags(number_of_tags,  user_id=TEST_USER_ID, repository_id=TEST_REPOSITORY_ID, tag_name=TEST_TAG_NAME):
    for tag_id in range(number_of_tags):
        RepositoryTag.objects.create(
            user_id=user_id,
            repository_id=repository_id,
            name=f'{tag_name}-{tag_id}'
        )


def get_tag(user_id, repository_id, tag_name):
    return RepositoryTag.objects.get(
        user_id=user_id,
        repository_id=repository_id,
        name=tag_name
    )


def api_create_tag(client, repository_id=TEST_REPOSITORY_ID, tag_name=TEST_TAG_NAME):
    url = reverse('repository_tags-list')
    data = {'repository_id': repository_id, 'name': tag_name}
    return client.post(url, data)


def api_list_tags(client):
    url = reverse('repository_tags-list')
    return client.get(url)


def api_delete_tag(client, tag_id):
    url = reverse('repository_tags-detail', args=(tag_id,))
    return client.delete(url)


class RepositoryTagTests(APITestCase):
    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION=TEST_ACCESS_TOKEN)

    def test_create_tag(self):
        response = api_create_tag(self.client)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RepositoryTag.objects.count(), 1)
        self.assertEqual(RepositoryTag.objects.get().name, TEST_TAG_NAME)

    def test_create_tag_duplicate(self):
        create_tag()
        response = api_create_tag(self.client)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(RepositoryTag.objects.count(), 1)

    def test_create_tag_unauthorized(self):
        self.client.credentials()
        response = api_create_tag(self.client)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(RepositoryTag.objects.count(), 0)

    def test_list_tags(self):
        number_of_tags = 10
        create_list_of_tags(number_of_tags)
        response = api_list_tags(self.client)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), number_of_tags)

    def test_list_tags_unauthorized(self):
        self.client.credentials()
        response = api_list_tags(self.client)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_tag(self):
        create_tag()
        tag = get_tag(TEST_USER_ID, TEST_REPOSITORY_ID, TEST_TAG_NAME)
        response = api_delete_tag(self.client, tag.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_tag_unauthorized(self):
        self.client.credentials()
        response = api_delete_tag(self.client, 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
