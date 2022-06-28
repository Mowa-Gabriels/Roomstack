from dataclasses import field
import imp
from django import forms
from django.forms import ModelForm
from authentication.models import *
from iroomie.models import *


class AddRoomForm(ModelForm):
    additional_amenity = forms.ModelMultipleChoiceField(
        queryset=Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    room_display_image_two = forms.ImageField(required=False)
    room_display_image_three = forms.ImageField(required=False)
    room_display_image_four = forms.ImageField(required=False)

    class Meta:

        model = Room
        exclude =(
            'owner',
            'slug',
        )

    



class EditRoomForm(ModelForm):
    additional_amenity = forms.ModelMultipleChoiceField(
        queryset=Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        room_display_image_two = forms.ImageField(required=False)
        room_display_image_three = forms.ImageField(required=False)
        room_display_image_four = forms.ImageField(required=False)

        model = Room
        exclude =(
            'owner',
            'slug',
        )
        widgets ={
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'col':10})
        }


class AddReviewForm(ModelForm):
    
    
    class Meta:

        model = Review
        fields =[
            'title',
            'experience',
        ]
