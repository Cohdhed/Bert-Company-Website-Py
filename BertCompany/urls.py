from pydoc import doc
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("bertapp.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)