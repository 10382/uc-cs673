from django.conf.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    path('', include('landing.urls')),
    path('chat/', include('chat.urls')), # redirect to chat.urls
    path('about/', include('about.urls')), # redirect to about.urls
    path('users/', include('users.urls')), # redirect to users.urls
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
