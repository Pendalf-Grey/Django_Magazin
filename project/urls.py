from django.contrib import admin
from django.urls import path, include
from .settings import DEBUG
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('main.urls', namespace='main')),

    path('catalog/', include('goods.urls', namespace='catalog')),

    path('user/', include('users.urls', namespace='user')),

    path('carts/', include('carts.urls', namespace='carts')),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
