from rest_framework import serializers

from apps.accounts.models import User
from apps.mail.models import Mail

class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )

    class Meta:
        model = User
        fields = ['id', 'name', 'phone_number', 'password']


class UserDatailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['name', 'phone_number']

class MessageSerializer(serializers.ModelSerializer):

    sender = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())
    receiver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())

    class Meta:
        model = Mail
        fields = ['id', 'sender', 'receiver', 'message', 'timestamp']