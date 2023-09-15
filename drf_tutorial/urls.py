from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from post.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", home, name="home"),
    path("api/posts/", include("post.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
