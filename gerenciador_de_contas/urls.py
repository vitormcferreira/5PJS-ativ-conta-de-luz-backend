from django.urls import include, path
from rest_framework import routers
from contas import views

# https://www.django-rest-framework.org/api-guide/routers/#defaultrouter
# list -> GET {prefix}/
# create -> POST {prefix}/
# retrieve -> GET {prefix}/{lookup}/[.format]
# update -> PUT {prefix}/{lookup}/[.format]
# partial_update -> PATCH {prefix}/{lookup}/[.format]
# destroy -> DELETE {prefix}/{lookup}/[.format]
router = routers.DefaultRouter()
router.register(r'contas', views.ContaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
