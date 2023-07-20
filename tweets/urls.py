from django.urls import path

from .views import tweet_detail_view, tweet_action_view, tweets_list_view, tweet_create_view, tweet_delete_view

urlpatterns = [
    path('', tweets_list_view, name='tweet_list'),
    path('create-tweet/', tweet_create_view, name='tweet_create'),
    path('<int:tweet_id>', tweet_detail_view, name='tweet_detail'),
    path('api/tweets/action', tweet_action_view),
    path('api/<int:tweet_id>/delete', tweet_delete_view, name='tweet_delete'),
    ]