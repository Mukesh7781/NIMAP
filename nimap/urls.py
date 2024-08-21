from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from nimap import views

router = DefaultRouter()
router.register(r'clients', views.ClientViewSet)
router.register(r'projects', views.ProjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nimap/', include(router.urls)),
]
