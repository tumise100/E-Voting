from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
from Vote.models import User

class UsernameBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        Matric = kwargs['username']

        try:
            student = User.objects.get(Matric=Matric)

            return student
        except User.DoesNotExist:
            pass

    def get_user(self, User_id):
        try:
            return User.objects.get(pk=User_id)
        except User.DoesNotExist:
            return None

