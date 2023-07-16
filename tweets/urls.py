from django.urls import path

from .views import tweet_detail_view, tweets_list_view, tweet_create_view, tweet_delete_view

urlpatterns = [
    path('', tweets_list_view, name='tweet_detail'),
    path('create-tweet/', tweet_create_view, name='tweet_detail'),
    path('<int:tweet_id>', tweet_detail_view, name='tweet_detail'),
    path('api/<int:tweet_id>/delete', tweet_delete_view, name='tweet_detail'),
    ]