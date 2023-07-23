from django.urls import path

from .views import tweet_detail_view, tweet_action_view, tweets_list_view, tweet_create_view, tweet_delete_view

app_name = 'tweets'

urlpatterns = [
    path('', tweets_list_view, name='tweets_list'),
    path('action/', tweet_action_view, name="tweet_action"),
    path('create/', tweet_create_view, name='tweet_create'),
    path('<int:tweet_id>/', tweet_detail_view, name='tweet_detail'),
    path('<int:tweet_id>/delete/', tweet_delete_view, name='tweet_delete'),
    ]