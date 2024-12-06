from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

@api_view(['POST'])
# @permission_classes([AllowAny])
def login(request):
   user = None
   try:
      print(request.data['email'])
      user = User.objects.get(email=request.data['email'])
   except:
      raise AuthenticationFailed(detail="Credenciales inválidas")
   
   if not user.check_password(request.data['password']):
      raise AuthenticationFailed(detail="Credenciales inválidas")
   
   return Response({ "detail": "User logged", "user": { "email": user.email, "id": user.id }}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
   serializer = UserSerializer(data=request.data)
   if serializer.is_valid():
      serializer.save()
      user = User.objects.get(email=request.data['email'])
      user.username = request.data['email'].split("@")[0] 
      user.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
   
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def checktoken(request):
   user = get_object_or_404(User, email=request.user.email)
   serializer = UserSerializer(instance=user)
   return Response({"user": serializer.data, "permissions": user.get_all_permissions()})