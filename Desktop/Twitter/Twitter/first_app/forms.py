from django import forms
from main_app.models import Tweet, User

class TweetForm(forms.Form):
    text = forms.CharField(max_length=140, widget=forms.Textarea)

