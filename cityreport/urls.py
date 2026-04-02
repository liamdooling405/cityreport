"""
URL configuration for cityreport project.
"""

from django.contrib import admin
from django.urls import path, include

# For media files (image uploads)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    # Connect your app
    path('', include('issues.urls')),
]

# Serve uploaded images during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)