from django.urls import path, include
from rest_framework import routers
from snsbackend.views import SnsPostViewSet, LoginAPIView, create_user
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'snsposts', SnsPostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api/login/', LoginAPIView.as_view(), name='login'),
    path('api/signup/', create_user, name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
