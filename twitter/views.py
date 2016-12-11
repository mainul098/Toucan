from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from twitter.forms import TweetFrom
from twitter.models import Follow
from .forms import UserForm
from .models import Tweet


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'twitter/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('twitter:index')
            else:
                return render(request, 'twitter/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'twitter/login.html', {'error_message': 'Invalid login'})
    return render(request, 'twitter/login.html')


def register_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('twitter:index')
    context = {
        "form": form,
    }
    return render(request, 'twitter/register.html', context)


@login_required(login_url='twitter:login_user')
def index(request):
    if not request.user.is_authenticated():
        return render(request, 'twitter/login.html')
    else:
        latest_tweets = Tweet.objects.filter(user__followers__user=request.user).order_by(
            '-modified_date') | Tweet.objects.filter(user=request.user).order_by('-modified_date')
        candidate_follower = User.objects.exclude(followers__user=request.user).exclude(username=request.user.username)
        context = {
            'latest_tweets': latest_tweets,
            'followers': User.objects.filter(followers__user=request.user),
            'candidate_follower': candidate_follower
        }

        return render(request, 'twitter/index.html', context)


@login_required(login_url='twitter:login_user')
def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    latest_tweets = Tweet.objects.filter(user=user)

    context = {
        'latest_tweets': latest_tweets,
        'user_info': user
    }
    return render(request, 'twitter/index.html', context)


@login_required(login_url='twitter:login_user')
def create_tweet(request):
    form = TweetFrom(request.POST or None)

    if form.is_valid():
        tweet = form.save(commit=False)
        tweet.user = request.user
        tweet.save()

    return redirect('twitter:index')


@login_required(login_url='twitter:login_user')
def add_follow(request, user_id):
    follower = get_object_or_404(User, pk=user_id)
    follow = Follow(user=request.user, follower=follower)
    follow.save()
    return redirect('twitter:index')


@login_required(login_url='twitter:login_user')
def remove_follow(request, user_id):
    follower = Follow.objects.get(follower_id=user_id, user=request.user)

    if follower is not None:
        follower.delete()

    return redirect('twitter:index')
