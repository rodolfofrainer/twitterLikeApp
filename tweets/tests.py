from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import TweetsModel

User = get_user_model()

class TweetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='some_random_user', password='some_random_password')

    def test_tweet_created(self):
        tweet_obj = TweetsModel.objects.create(content='Some random content', user=self.user)
        self.assertEqual(tweet_obj.id, 1)
        self.assertEqual(tweet_obj.user, self.user)

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='some_random_password')
        return client

    def test_tweet_list(self):
        client = self.get_client()
        url = reverse('tweets:tweets_list')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        print(response)
