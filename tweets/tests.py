from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import TweetsModel

User = get_user_model()

class TweetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='some_random_user', password='some_random_password')
        TweetsModel.objects.create(content='my first tweet', user=self.user)
        TweetsModel.objects.create(content='my first tweet', user=self.user)
        TweetsModel.objects.create(content='my first tweet', user=self.user)
        

    def test_tweet_created(self):
        tweet_obj = TweetsModel.objects.create(content='my second tweet', user=self.user)
        self.assertEqual(tweet_obj.id, 4)
        self.assertEqual(tweet_obj.user, self.user)

    def get_client(self):
        client = APIClient()
        token, _ = Token.objects.get_or_create(user=self.user)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        return client

    def test_tweet_list(self):
        client = self.get_client()
        url = reverse('tweets:tweets_list')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)
        
    def test_action_like(self):
        client = self.get_client()
        url = reverse('tweets:tweet_action')
        data = {'id': 1, 'action': 'like'}
        response = client.post(url, data)
        self.assertEqual(response.status_code, 200)
        print(response.json())