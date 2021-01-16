from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

app_name = 'store'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls', namespace='store')),
    path('acc/', include('user.urls', namespace='user'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'store.views.handler404'
handler500 = 'store.views.handler500'