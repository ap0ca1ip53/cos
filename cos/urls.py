from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [
        url(r'^auth/', include('django.contrib.auth.urls', namespace='auth')),
        url(r'^', include('core.urls', namespace='core')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)