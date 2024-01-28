from django.contrib import admin
from django.urls import path, include
from .settings import DEBUG
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('main.urls', namespace='main')),

    path('catalog/', include('goods.urls', namespace='catalog')),

    path('user/', include('users.urls', namespace='user')),

    # path('cart/', include('cart.urls', namespace='cart')),

]

if DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
