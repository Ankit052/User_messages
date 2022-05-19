
from .models import Message
from .serializers import MessageSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 

# Create your views here.

# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token

# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)



class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # permission_classes = (IsAuthenticated,)
