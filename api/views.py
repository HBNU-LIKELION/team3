from rest_framework.viewsets import ModelViewSet
from .models import Info
from .serializers import InfoModelSerializer

class InfoViewSet(ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoModelSerializer