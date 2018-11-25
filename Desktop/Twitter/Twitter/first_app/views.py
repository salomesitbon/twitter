from django.shortcuts import render, redirect
from main_app.models import User, Tweet
from . import forms
import datetime


def index(request):
	tweets = Tweet.objects.all().order_by('-date')[:30]
	return render(request, 'index.html', { 'tweets': tweets })


def profile(request, user_id):
	user   = User.objects.get(id=user_id)
	tweets = Tweet.objects.filter(user=user_id)[:5]
	return render(request, 'profile.html', { 'tweets': tweets, 'user': user})


def create_tweet(request, user_id):
	user   = User.objects.get(id=user_id)
	form   = forms.TweetForm()

	if request.method == 'POST':
		form = forms.TweetForm(request.POST)
		if form.is_valid():
			text  = form.cleaned_data['text']
			tweet = Tweet(text=text, user=user, date=datetime.datetime.now())
			tweet.save()
			return redirect('/main_app/')

	return render(request, 'tweetform.html', {'form': form, 'user': user})


