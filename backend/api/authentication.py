from rest_framework import authentication
from rest_framework import exceptions
from apps.accounts.models import User


class ExampleAuthentication(authentication.BaseAuthentication):

    def has_object_permission(self, request, *args, **kwargs):
        return getattr(request.user, 'phone_number', None)

    def has_permission(self, request, view):
        return getattr(request.user, 'phone_number', None)

    def authenticate(self, request, *args, **kwargs):
        phone_number = request.META.get('HTTP_X_USERNAME') # get the phone_number request header

        if not phone_number: # no phone_number passed in request headers
            return None # authentication did not succeed

        try:
            user = User.objects.get(phone_number=phone_number) # get the user
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user') # raise exception if user does not exist

        return (user, None) # authentication successful