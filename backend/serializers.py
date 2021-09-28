from rest_framework import serializers

from backend.models import RepositoryTag


class RepositoryTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepositoryTag
        fields = ('id', 'repository_id', 'name')
