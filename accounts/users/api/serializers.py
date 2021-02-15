from rest_framework.serializers import ModelSerializer
from accounts.users.models import User

class BaseUserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'


class SignupUserSerializer(BaseUserSerializer):
  class Meta:
    fields = ['username', 'password']






