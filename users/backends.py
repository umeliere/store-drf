from django.contrib.auth.backends import ModelBackend, get_user_model
from django.db.models import Q

UserModel = get_user_model()


class UserModelBackend(ModelBackend):
    """
    The class that allows to log in using the email and the login
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def get_user(self, user_pk):
        try:
            user = UserModel.objects.get(pk=user_pk)
        except UserModel.DoesNotExist:
            return None

        return user if self.user_can_authenticate(user) else None
