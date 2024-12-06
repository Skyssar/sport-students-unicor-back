from rest_framework import viewsets
from .serializers import ProfileInfoSerializer, SportHistoryInfoSerializer, SportHistorySerializer, SportSerializer, UserSerializer
from .models import Profile, SportHistoryInfo, SportHistory, Sport
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.db import IntegrityError
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet): 
   queryset = Profile.objects.all()
   serializer_class = ProfileInfoSerializer

class BasicInfoViewSet(viewsets.ModelViewSet): 
   queryset = Profile.objects.all()
   serializer_class = ProfileInfoSerializer

   def create(self, request):
      data = request.data.copy();
      user_id = data.pop('user');
      profile, created = Profile.objects.update_or_create(
         user_id=user_id, defaults=data)
      return Response('Saved', status=status.HTTP_200_OK)


class SportHistoryInfoViewSet(viewsets.ModelViewSet): 
   queryset = SportHistoryInfo.objects.all()
   serializer_class = SportHistoryInfoSerializer
   parser_classes = ( MultiPartParser, FormParser, JSONParser )

   def create(self, request):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      data= serializer.validated_data
      
      # Extraer el usuario de los datos validados
      user = data['user']
         
      try:
         defaults = {field: data[field] for field in data if field != 'user'};
         instance, created = SportHistoryInfo.objects.update_or_create(
               user=user,  # Criterio único basado en OneToOneField
               defaults=defaults
         )
         mensaje = 'Creado' if created else 'Actualizado'
         return Response({
               'mensaje': mensaje,
               'data': self.get_serializer(instance).data
         }, status=status.HTTP_200_OK)

      except IntegrityError:
         return Response(
               {"error": "Un registro para este usuario ya existe y no se pudo actualizar."},
               status=status.HTTP_400_BAD_REQUEST
         )
         
      # profile, created = SportHistoryInfo.objects.update_or_create(
      #    user_id=data["user"], defaults={ **data, "user": user_instance })
      return Response('Saved', status=status.HTTP_200_OK)

class SportHistoryViewSet(viewsets.ModelViewSet): 
   queryset = SportHistory.objects.all()
   serializer_class = SportHistorySerializer

   # Verificar si el payload es una lista
   def create(self, request, *args, **kwargs):
      if isinstance(request.data, list):
         serializer = self.get_serializer(data=request.data, many=True)
      else:
         serializer = self.get_serializer(data=request.data)

      serializer.is_valid(raise_exception=True)
      objects = SportHistory.objects.filter(user_id = request.data[0]["user"])
      if objects: objects.delete();
      self.perform_create(serializer)

      return Response(
         serializer.data,
         status=status.HTTP_201_CREATED
      )
   
class SportViewSet(viewsets.ModelViewSet): 
   queryset = Sport.objects.all()
   serializer_class = SportSerializer