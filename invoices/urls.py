from django.urls import path, include
from .routers import SlashOptionalRouter

from .views.person_views import PersonViewSet

router = SlashOptionalRouter()
router.register(r'persons', PersonViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
