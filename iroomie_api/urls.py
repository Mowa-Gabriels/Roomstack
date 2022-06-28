from .views import UserList
from django.urls import path



urlpatterns = [
    path('user/', UserList.as_view(), name='user'),
    
    
]
