
from django.forms import ModelForm
from .models import *

class NewsletterForm(ModelForm):

    class Meta:
        model =  Newsletter
        fields = [
            'email'
        ]
