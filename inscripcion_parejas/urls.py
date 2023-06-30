
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from inscripcion_parejas import views 

router = routers.DefaultRouter()    
router.register(r'inscripcion_parejas', views.InscripcionParejasViewSet, basename='inscripcion_parejas')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls (title=' Parejas'))
]
    
