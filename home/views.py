
from .models import Message
from .serializers import MessageSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.throttling import UserRateThrottle
from rest_framework.authentication import TokenAuthentication

# Create your views here.

# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token

# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)



class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    throttle_classes = [UserRateThrottle]
