"""Main URLs module."""

from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include(('rwu.users.urls', 'users'), namespace='users')),
    path('', include(('rwu.employees.urls', 'employees'), namespace='employees')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
