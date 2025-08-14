from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",include('home.urls')),
    path("profile/",include('Profile.urls')),
    path("api/",include('api.urls')),
    path('silk/', include('silk.urls', namespace='silk')),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
]