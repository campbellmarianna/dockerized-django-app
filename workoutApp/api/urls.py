from django.conf.urls import url, include

from rest_framework import routers

from api.views import RepViewSet, SetViewSet, WorkoutViewSet

router = routers.DefaultRouter()

router.register(r'rep', RepViewSet)
router.register(r'set', SetViewSet)
router.register(r'workout', WorkoutViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'auth/', include('rest_framework.urls'))
]
