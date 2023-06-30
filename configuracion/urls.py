
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from configuracion import views 

router = routers.DefaultRouter()
router.register(r'configuracion', views.ConfiguracionViewSet, basename='configuracion')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls (title='Campeonato '))
]
    
