from django.urls import path, include
from .routers import SlashOptionalRouter

from .views.person_views import PersonViewSet

from .views.invoice_views import InvocieViewSet


router = SlashOptionalRouter()
router.register(r'persons', PersonViewSet)
router.register(r'invoices', InvocieViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
