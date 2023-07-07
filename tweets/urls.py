from django.urls import path

from .views import tweet_detail_view, tweets_list_view, tweet_create_view

urlpatterns = [
    path('<int:tweet_id>', tweet_detail_view, name='tweet_detail'),
    path('create-tweet/', tweet_create_view, name='tweet_detail'),
    path('', tweets_list_view, name='tweet_detail'),
    ]