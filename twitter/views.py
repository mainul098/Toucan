from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from twitter.models import get_follower_tweets, Tweet


def index(request):
    latest_tweets = Tweet.objects.order_by('created_date')
    context = {'latest_tweets': latest_tweets}
    return render(request, 'twitter/index.html', context)


@login_required
def timeline(request):
    user = request.user
    tweets = get_follower_tweets(user)
    return render(request, 'timeline.html', {'tweets': tweets, 'user': user})
