import django_filters
from .models import *
from authentication.models import *

class RoomFilter(django_filters.FilterSet):
    #name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Room
        fields = ['type', 'school', 'rent_range', 'bills', 'room_composition', 'stay_duration', 'home_furnishing']


class ProfileFilter(django_filters.FilterSet):
    #name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = User
        fields = ['action', 'school', 'sex']

class PreferenceFilter(django_filters.FilterSet):
    course_of_interest = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = User
        fields = [

    'pets_allowed' ,
    'smoking_allowed', 
    'pref_age_range', 
    'pref_religion', 
    'room_clean', 
    'room_noise', 
    'out_of_towners', 
    'family_visits', 
    'course_of_interest', 
   
        ]