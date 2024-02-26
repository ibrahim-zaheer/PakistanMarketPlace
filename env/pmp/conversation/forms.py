from django.forms import forms

from .models import conversationMessage
class conversationMessageForm(forms.ModleForm):
    class Meta:
        model = conversationMessage
        fields = {'content',}