from django.urls import path, include
from rest_framework import routers
from .api import BasicInfoViewSet, SportHistoryInfoViewSet, SportHistoryViewSet, SportViewSet, UserViewSet
from . import views

router = routers.SimpleRouter()
router.register(r'profile-info', BasicInfoViewSet, basename='profile-info')
router.register(r'sport-info', SportHistoryInfoViewSet, basename='sport-info')
router.register(r'sports-history', SportHistoryViewSet, basename='sports-history')
router.register(r'sports', SportViewSet, basename='sports')
router.register(r'users', UserViewSet, basename='usuarios')
# router.register(r'get-location', get_location_info, basename='get-location')

urlpatterns = [
   path('', include( router.urls )),
   path('login', views.login),
   path('signup', views.signup),
] 
