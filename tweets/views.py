from django.shortcuts import render
from django.http import HttpResponse,Http404, JsonResponse

from .models import TweetsModel

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'tweets/home.html', context={}, status=200)

def tweets_list_view(request, *args, **kwargs):
    """
    Consume by JS
    return json data

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    qs = TweetsModel.objects.all()
    tweets_list = [{"id": x.id, "content": x.content} for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)
    
def tweet_detail_view(request,tweet_id, *args, **kwargs):
    """
    Rest API view

    Args:
        request (HttpResponse)
        tweet_id (int)

    Raises:
        Http404: Raise 404 error if tweet_id is not found

    Returns:
        JsonData: Returns Json data
    """
    
    context = {
        "id": tweet_id,
    }
    status = 200
    
    try:
        obj = TweetsModel.objects.get(id=tweet_id)
        context['content'] = obj.content
    except:
        context['message'] = "Not Found"
        status = 404
    return JsonResponse(context, status=status)