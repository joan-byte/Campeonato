from rest_framework import viewsets
from .models import caracteristicas_campeonato
from .serializers import ConfiguracionSerializer

class ConfiguracionViewSet(viewsets.ModelViewSet):
    queryset = caracteristicas_campeonato.objects.all()
    serializer_class = ConfiguracionSerializer