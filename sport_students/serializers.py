from rest_framework import serializers
from .models import Profile, SportHistoryInfo, SportHistory, Sport
from django.contrib.auth.models import User

class UserSerializer( serializers.ModelSerializer ):
   password = serializers.CharField(min_length=8, write_only=True)
   class Meta(object):
      model = User
      fields = [ 'id', 'email', 'password' ]
      read_only_fields = ['id']

   def validate_email(self, value):
      # Verifica si ya existe un usuario con el mismo correo
      if User.objects.filter(email=value).exists():
         raise serializers.ValidationError("El correo ya está registrado.")
      return value

class ProfileInfoSerializer( serializers.ModelSerializer ):
   email = serializers.EmailField(source="user.email", read_only=True)
   birthday = serializers.DateField(format="%d-%m-%Y")

   class Meta(object):
      model = Profile
      fields = "__all__"

class SportHistorySerializer( serializers.ModelSerializer ):
   class Meta(object):
      model = SportHistory
      fields = "__all__"

class SportHistoryInfoSerializer( serializers.ModelSerializer ):
   sports = SportHistorySerializer( many=True, read_only=True )
   user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
   class Meta(object):
      model = SportHistoryInfo
      fields = "__all__"

   def validate_user(self, value):
      print("validating")
      """
      Validar que no se cree un registro duplicado para el usuario.
      Solo se valida si estamos creando un nuevo registro, no cuando estamos actualizando.
      """
      return value

class SportSerializer( serializers.ModelSerializer ):
   class Meta(object):
      model = Sport
      fields = "__all__"