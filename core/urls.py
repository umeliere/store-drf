from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.yasg import urlpatterns as docs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/carts/', include('cart.urls', namespace='cart')),
    path('api/v1/orders/', include('orders.urls', namespace='orders')),
    path("api/v1/auth/", include("users.urls", namespace='users')),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.authtoken")),
    path("api/v1/", include('store.urls', namespace='store')),
    path("api-auth/", include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + docs

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
