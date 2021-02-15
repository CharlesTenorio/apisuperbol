from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
# from rest_framework.authentication import TokenAuthentication
from accounts.users.models import User
from accounts.users.api.serializers import BaseUserSerializer

class UserViewSet(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = BaseUserSerializer
  permission_classes = [IsAdminUser]
  authentication_classes = []

class CreateUserViewset(CreateAPIView):
  queryset = User.objects.all()
  serializer_class = BaseUserSerializer
