from email import message
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# from .utils import IsOwnerOrReadOnly 
from authentication.models import User
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.reverse import reverse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
   

    



class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
 
    