from django.db import models


class RepositoryTag(models.Model):
    user_id = models.IntegerField()
    repository_id = models.IntegerField()
    name = models.CharField(max_length=100)


class GitHubUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    oauth_token = models.TextField()
