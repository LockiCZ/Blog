from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('dj-admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('user/', include('allauth.urls')),
    path('martor/', include('martor.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
