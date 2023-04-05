from django.contrib import admin
from django.urls import path,  include
from rest_framework.routers import DefaultRouter
from asosiy.views import *
from rest_framework_simplejwt.views import (TokenRefreshView, TokenObtainPairView,)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Omborxona API",
      default_version='v1',
      description="Omborxona hisobini yuritish",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact("Akmaljon Fayzullayev, <akmaljonfayzullayev07@gmail.com>"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register('omborlar', OmborViewSet)
router.register('stats', StatsViewSet)
router.register('mahsulotlar', MahsulotViewSet)
router.register('clientlar', ClientViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('token_ber/', TokenObtainPairView.as_view()),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('token_yangila/', TokenRefreshView.as_view()),
]
