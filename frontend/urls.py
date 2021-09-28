from django.urls import include, re_path

from frontend import views

urlpatterns = [
    re_path(r'^', views.frontend),
]
