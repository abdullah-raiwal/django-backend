from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='api-docs'),
    path('api/user/', include('user.urls')),

]
