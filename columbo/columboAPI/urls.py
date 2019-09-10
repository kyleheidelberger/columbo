from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'episodes', views.EpisodeViewSet)
router.register(r'seasons', views.SeasonViewSet)
router.register(r'characters', views.CharacterViewSet)
router.register(r'actors', views.ActorViewSet)
router.register(r'writers', views.WriterViewSet)
router.register(r'directors', views.DirectorViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
