from rest_framework import routers
from .views import PostViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = router.urls
