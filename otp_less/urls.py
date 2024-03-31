from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('api.v1.auth.urls', namespace='api_v1_authentication')),
]
