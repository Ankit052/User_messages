from rest_framework import serializers
from .models import Message
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'email')

class MessageSerializer(serializers.ModelSerializer):


    class Meta :
        model = Message 
        fields = ["id","message","created_at","updated_at","created_by"]


    def to_representation(self, instance):
        data = super(MessageSerializer, self).to_representation(instance)     
        data["created_by"] = UserSerializer(instance.created_by).data

        return data
    




