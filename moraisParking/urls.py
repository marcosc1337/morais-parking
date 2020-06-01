from django.contrib import admin
from django.urls import path, include
from core import urls as core_urls
from accounts import urls as accounts_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urls)),
    path('accounts/', include(accounts_urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]
