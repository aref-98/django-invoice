from django.urls import path, include
from .routers import SlashOptionalRouter

from .views.person_views import PersonViewSet

from .views.invoice_views import InvoiceViewSet
from .views.identification_views import sales_by_identification, purchases_by_identification


router = SlashOptionalRouter()
router.register(r'persons', PersonViewSet)
router.register(r'invoices', InvoiceViewSet, basename='invoice')

urlpatterns = [
    
    path('api/', include(router.urls)),
    path('api/identification/<str:ico>/sales', sales_by_identification),
    path('api/identification/<str:ico>/purchases', purchases_by_identification),

    
]
