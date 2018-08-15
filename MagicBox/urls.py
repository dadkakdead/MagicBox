from django.contrib import admin
from django.urls import path

urlpatterns = []

from django.conf.urls import include
from django.urls import path

urlpatterns += [
    path('webrequest/', include('webrequest.urls')),
]

from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='webrequest/'))
]

from django.conf.urls import url
from django.contrib import admin

urlpatterns += [
    path(r'accounts/', include('django.contrib.auth.urls')),
    url(r'admin/', admin.site.urls),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
