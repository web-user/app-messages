from rest_framework.generics import ListCreateAPIView, GenericAPIView
# from rest_framework_jwt.settings import api_settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import mixins
from django.http import JsonResponse

from apps.accounts.models import User
from apps.mail.models import Mail
from .serializers import UserSerializer, MessageSerializer
from api.authentication import ExampleAuthentication


class MessageList(ListCreateAPIView):
    """
    View Message List
    """
    # permission_classes = (ExampleAuthentication,)
    queryset = Mail.objects.all()
    serializer_class = MessageSerializer


class InboxMessageList(viewsets.ViewSet):
    """
    View Message List
    """
    # permission_classes = (ExampleAuthentication,)
    def list(self, request):
        user = request.user
        queryset = Mail.objects.filter(receiver__phone_number=user.phone_number)
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)


class SentMessageList(viewsets.ViewSet):
    """
    View Sent Message List
    """
    # permission_classes = (ExampleAuthentication,)
    def list(self, request):
        user = request.user
        queryset = Mail.objects.filter(sender__phone_number=user.phone_number)
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)


class UserList(ListCreateAPIView):
    """
    View is used for create User
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class SentMessageUserList(viewsets.ViewSet):
    """
    View is used for create User
    """

    def list(self, request):
        user = request.user
        queryset = User.objects.exclude(phone_number=user.phone_number)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

class UserDetailUpdateDestroy(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericAPIView):
    """
    View is used for get / update / delete Student
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class MessageDetailDestroy(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericAPIView):
    """
    View is used for get / update / delete Message
    """
    queryset = Mail.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


def home(request):
    return JsonResponse(data={"message": "success"}, status=200)
