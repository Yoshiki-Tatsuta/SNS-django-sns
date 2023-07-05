from django.urls import path, include
from rest_framework import routers
from snsbackend.views import SnsPostViewSet, LoginAPIView
from django.views.decorators.csrf import get_token
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'snsposts', SnsPostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api/login/', LoginAPIView.as_view(), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
