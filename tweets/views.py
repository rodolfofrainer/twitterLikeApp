import random

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings

from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import TweetsModel
from .forms import TweetsForm
from .serializers import TweetSerializer

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'tweets/home.html', context={}, status=200)

@api_view(['Post'])
# @authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def tweet_create_view(request, *args, **kwargs):
    data = request.POST
    serializer = TweetSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)

@api_view(['GET'])
def tweets_list_view(request, *args, **kwargs):
    qs = TweetsModel.objects.all()
    serializer = TweetSerializer(qs, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    qs = TweetsModel.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({}, status=404)
    obj=qs.first()
    serializer = TweetSerializer(obj)
    return Response(serializer.data, status=200)


def tweet_create_view_pure_django(request, *args, **kwargs):
    """
    REST API Create View
    """
    user = request.user
    if not request.user.is_authenticated:
        user = None
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)
    is_ajax = bool(request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest')
    form = TweetsForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj=form.save(commit=False)
        obj.user = request.user or None
        obj.save()
        if is_ajax:
            return JsonResponse(obj.serialize(), status=201) # 201 == created items
        if next_url != None and url_has_allowed_host_and_scheme(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetsForm()
    if form.errors:
        if is_ajax:
            return JsonResponse(form.errors, status=400)
    context = {'form': form}
    return render(request, 'tweets/form.html', context=context, status=200)

def tweets_list_view_pure_django(request, *args, **kwargs):
    """
    Consume by JS
    return json data

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    qs = TweetsModel.objects.all()
    tweets_list = [x.serialize() for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)
    
def tweet_detail_view_pure_django(request,tweet_id, *args, **kwargs):
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