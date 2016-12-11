from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from .models import Tweet


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'twitter/login.html')
    else:
        latest_tweets = Tweet.objects.order_by('created_date')
        return render(request, 'twitter/index.html', {'latest_tweets': latest_tweets})


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
                latest_tweets = Tweet.objects.order_by('created_date')
                return render(request, 'twitter/index.html', {'latest_tweets': latest_tweets})
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
                latest_tweets = Tweet.objects.order_by('created_date')
                return render(request, 'twitter/index.html', {'latest_tweets': latest_tweets})
    context = {
        "form": form,
    }
    return render(request, 'twitter/register.html', context)

