from django import forms
from .models import TweetsModel

MAX_TWEET_LENGTH = 240

class TweetsForm(forms.ModelForm):
  
    class Meta:
        model = TweetsModel
        fields = ('content',)
    
    def clean_content(self):
        content= self.cleaned_data.get("content")
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("This tweet is too long")
        return content