from django.urls import path

from .views import tweet_detail_view

urlpatterns = [
    path('<int:tweet_id>', tweet_detail_view, name='tweet_detail')]