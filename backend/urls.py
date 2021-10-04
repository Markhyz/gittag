from django.urls import include, path
from rest_framework.routers import DefaultRouter

from backend import views

router = DefaultRouter()
router.register('tags', views.RepositoryTagViewSet,
                basename='repository_tags')

urlpatterns = [
    path('', include(router.urls)),
    path('auth', views.GitHubAuth.as_view(), name='auth'),
    path('github/user', views.get_github_user, name='github-user'),
    path('github/user/starred', views.get_github_user_starred, name='github-starred')
]
