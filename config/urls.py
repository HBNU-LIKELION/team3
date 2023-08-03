from django.urls import path, include
from rest_framework import routers
from api.views import InfoViewSet


router = routers.DefaultRouter()
router.register('sites',InfoViewSet)

urlpatterns = [
    path('',include(router.urls)),
]