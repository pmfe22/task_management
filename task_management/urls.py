from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from tasks.views import TaskViewSet  
from rest_framework.authentication import TokenAuthentication
from rest_framework.routers import DefaultRouter


# ایجاد API router
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

# تنظیمات Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Task Management API",
        default_version="v1",
        description="API for managing tasks",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@taskmanagement.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    authentication_classes=(TokenAuthentication,),
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include('tasks.urls')),     
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
    path('accounts/', include('django.contrib.auth.urls')),  

    
    path('api/', include(router.urls)),  
]

# برای دسترسی به فایل‌های استاتیک و رسانه‌ای
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
