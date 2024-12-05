from django.urls import path

from search.views import search_view as views

urlpatterns = [
    path("", views.YoutubeSearchAPI.as_view(), name="youtube-search"),
]
